// Antigravity Security+ (SY0-701) Study Portal App Logic

// --- Global State ---
let scheduleData = [];
let questionsData = [];
let flashcardsData = [];
let filteredFlashcards = [];
let videosData = {};
let pdfsData = [];

// New structured data
let studyDaysData = [];
let domainsData = {};
let examObjectivesData = [];

// Persistent user progress schema in localStorage
let userProgress = {
  checkedItems: {},
  completedDays: {},
  blockProgress: {},    // key: "day_X_reading" | "day_X_video" | "day_X_quiz", value: true
  popupQuizzes: {},     // key: "popup_slot_0..5", value: { score, total, completed: true }
};

// Quiz Session State
let quizSession = {
  mode: 'sim',
  questions: [],
  userAnswers: {},
  flaggedQuestions: {},
  currentIndex: 0,
  timeLeft: 0,
  timerInterval: null,
  startTime: 0,
  timeTaken: 0
};

// Popup Quiz State
let popupQuizState = {
  questions: [],
  userAnswers: {},
  currentIndex: 0,
  slotIndex: -1
};

// Flashcards State
let flashcardIndex = 0;
let isFlipped = false;

// Current video sub-objective (for split-screen reading)
let currentVideoSubObjective = null;

// --- Initialize App ---
document.addEventListener('DOMContentLoaded', () => {
  loadProgress();
  initRouter();
  loadData();
  setupEventListeners();
});

// --- LocalStorage Progress Management ---
function loadProgress() {
  const saved = localStorage.getItem('secplus_user_progress');
  if (saved) {
    try {
      userProgress = JSON.parse(saved);
      if (!userProgress.checkedItems) userProgress.checkedItems = {};
      if (!userProgress.completedDays) userProgress.completedDays = {};
      if (!userProgress.blockProgress) userProgress.blockProgress = {};
      if (!userProgress.popupQuizzes) userProgress.popupQuizzes = {};
    } catch (e) {
      console.error("Failed to parse user progress", e);
    }
  }
}

function saveProgress() {
  localStorage.setItem('secplus_user_progress', JSON.stringify(userProgress));
  updateOverallProgress();
}

function updateOverallProgress() {
  if (!studyDaysData.length) return;
  
  let completedCount = 0;
  studyDaysData.forEach(day => {
    const dayKey = `day_${day.day_id}`;
    const readingKey = `${dayKey}_reading`;
    const videoKey = `${dayKey}_video`;
    const quizKey = `${dayKey}_quiz`;
    
    // A day is complete if all 3 blocks are completed
    let allCompleted = false;
    
    // Day 29+ are review days, they don't follow the 3-block strict rule, but we mark them complete if their quiz block is done
    if (day.day_id >= 29) {
      allCompleted = !!userProgress.blockProgress[quizKey];
    } else {
      allCompleted = userProgress.blockProgress[readingKey] && 
                     userProgress.blockProgress[videoKey] && 
                     userProgress.blockProgress[quizKey];
    }
    
    if (allCompleted) {
      userProgress.completedDays[dayKey] = true;
      completedCount++;
    } else {
      delete userProgress.completedDays[dayKey];
    }
  });

  const percentage = Math.round((completedCount / 34) * 100);
  
  // Update UI Elements
  document.getElementById('progress-percentage').textContent = `${percentage}%`;
  document.getElementById('progress-bar-fill').style.width = `${percentage}%`;
  document.getElementById('progress-count').textContent = `${completedCount} of 34 Days Clear`;
  
  // Re-draw day statuses in dashboard grid
  renderDashboard();
  renderPopupQuizTracker();
}

// --- Routing Engine ---
function initRouter() {
  const menuButtons = document.querySelectorAll('.menu-btn');
  const panes = document.querySelectorAll('.pane');

  menuButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const paneId = btn.getAttribute('data-pane');
      
      // Update location hash to synchronize with our hash router
      if (location.hash !== `#${paneId}`) {
        location.hash = paneId;
      }
      
      // Active states in menu
      menuButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Swap viewpane
      panes.forEach(pane => {
        pane.classList.remove('active');
        if (pane.id === `pane-${paneId}`) {
          pane.classList.add('active');
        }
      });
      
      // Special actions on route enter
      // Pause any running videos when switching away
      const player = document.getElementById('video-player-element');
      if (player && paneId !== 'videos') {
        player.pause();
      }

      if (paneId === 'dashboard') {
        renderDashboard();
        renderPopupQuizTracker();
      } else if (paneId === 'modules') {
        renderModulesTree();
      } else if (paneId === 'flashcards') {
        initFlashcards();
      } else if (paneId === 'videos') {
        renderVideosTree();
      } else if (paneId === 'domains') {
        // Handled via hash routing, but force render if clicked
        renderDomainDeepDive('domain_1');
      } else if (paneId === 'objectives') {
        renderObjectivesBrowser();
      }
    });
  });
}

// --- Fetch Data Assets ---
async function loadData() {
  try {
    const [scheduleRes, questionsRes, flashcardsRes, videosRes, studyDaysRes, domainsRes, objectivesRes] = await Promise.all([
      fetch('./schedule.json'),
      fetch('./questions.json'),
      fetch('./flashcards.json'),
      fetch('./videos.json'),
      fetch('./study_days.json'),
      fetch('./domains.json'),
      fetch('./exam_objectives.json')
    ]);

    scheduleData = await scheduleRes.json();
    questionsData = await questionsRes.json();
    flashcardsData = (await flashcardsRes.json()).cards;
    videosData = await videosRes.json();
    studyDaysData = await studyDaysRes.json();
    domainsData = await domainsRes.json();
    examObjectivesData = await objectivesRes.json();

    // Optional: Load PDF guides manifest
    try {
      const pdfsRes = await fetch('./pdfs.json');
      if (pdfsRes.ok) {
        pdfsData = await pdfsRes.json();
      }
    } catch (e) {
      console.warn("pdfs.json manifest not found or empty yet", e);
    }

    renderDashboard();
    renderModulesTree();
    updateOverallProgress();
    
    // Process initial route if any hash is present
    handleHashRouting();
  } catch (err) {
    console.error("Failed to load portal JSON database files", err);
  }
}

// --- Event Listeners Setup ---
function setupEventListeners() {
  // Reset Progress Button
  document.getElementById('btn-reset-data').addEventListener('click', () => {
    if (confirm("Are you sure you want to reset all your checklist progress and exam statistics?")) {
      userProgress = { checkedItems: {}, completedDays: {} };
      saveProgress();
      renderDashboard();
    }
  });

  // Modal close buttons
  document.getElementById('btn-close-modal').addEventListener('click', () => {
    document.getElementById('day-modal').style.display = 'none';
  });
  window.addEventListener('click', (e) => {
    const modal = document.getElementById('day-modal');
    if (e.target === modal) {
      modal.style.display = 'none';
    }
  });

  // Practice engine mode switcher
  const modeSelect = document.getElementById('practice-mode');
  modeSelect.addEventListener('change', () => {
    const val = modeSelect.value;
    const domainGroup = document.getElementById('drill-domain-group');
    const countGroup = document.getElementById('drill-count-group');
    
    if (val === 'drill') {
      domainGroup.style.display = 'flex';
      countGroup.style.display = 'flex';
    } else {
      domainGroup.style.display = 'none';
      countGroup.style.display = 'none';
    }
  });

  // Start exam session
  document.getElementById('btn-start-practice').addEventListener('click', startPracticeSession);

  // Question navigation buttons
  document.getElementById('btn-prev-q').addEventListener('click', () => navigateQuestion(-1));
  document.getElementById('btn-next-q').addEventListener('click', () => navigateQuestion(1));
  document.getElementById('btn-flag-question').addEventListener('click', toggleFlagActiveQuestion);
  document.getElementById('btn-terminate-exam').addEventListener('click', () => {
    if (confirm("Terminate exam? Your progress will be lost.")) {
      endQuizUI();
    }
  });

  // Submit Exam
  document.getElementById('btn-submit-exam').addEventListener('click', submitExamHandler);
  
  // Close Alert
  document.getElementById('btn-close-alert').addEventListener('click', () => {
    document.getElementById('mandate-alert').style.display = 'none';
  });

  // Results Actions
  document.getElementById('btn-results-review').addEventListener('click', showReviewPane);
  document.getElementById('btn-results-close').addEventListener('click', () => {
    document.getElementById('practice-results').style.display = 'none';
    document.getElementById('practice-setup').style.display = 'block';
  });
  
  document.getElementById('btn-review-close-top').addEventListener('click', () => {
    document.getElementById('practice-review').style.display = 'none';
    document.getElementById('practice-results').style.display = 'block';
  });

  // Search Reading Modules
  const searchInput = document.getElementById('modules-search-input');
  searchInput.addEventListener('input', () => {
    renderModulesTree(searchInput.value.trim().toLowerCase());
  });

  // Flashcards flipper
  const cardContainer = document.getElementById('flashcard-container');
  cardContainer.addEventListener('click', () => {
    isFlipped = !isFlipped;
    if (isFlipped) {
      cardContainer.classList.add('flipped');
    } else {
      cardContainer.classList.remove('flipped');
    }
  });

  // Flashcard controls
  document.getElementById('btn-shuffle-flashcards').addEventListener('click', () => {
    shuffleDeck();
    flashcardIndex = 0;
    renderFlashcard();
  });
  document.getElementById('flashcards-filter').addEventListener('change', () => {
    filterDeck();
    flashcardIndex = 0;
    renderFlashcard();
  });
  document.getElementById('btn-prev-card').addEventListener('click', () => navigateCard(-1));
  document.getElementById('btn-next-card').addEventListener('click', () => navigateCard(1));

  // Search Video Lectures
  const videoSearchInput = document.getElementById('videos-search-input');
  if (videoSearchInput) {
    videoSearchInput.addEventListener('input', () => {
      renderVideosTree(videoSearchInput.value.trim().toLowerCase());
    });
  }

  // Domain view domain selector
  document.querySelectorAll('#domain-selector-bar .domain-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('#domain-selector-bar .domain-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      renderDomainDeepDive(tab.getAttribute('data-domain'));
    });
  });

  // Objectives browser search/filter
  const objSearch = document.getElementById('objectives-search');
  const objFilter = document.getElementById('objectives-domain-filter');
  if (objSearch && objFilter) {
    const renderObj = () => renderObjectivesBrowser(objSearch.value, objFilter.value);
    objSearch.addEventListener('input', renderObj);
    objFilter.addEventListener('change', renderObj);
  }

  // Split-screen video reading toggle
  const toggleReadingBtn = document.getElementById('btn-toggle-reading');
  const closeReadingBtn = document.getElementById('btn-close-reading');
  if (toggleReadingBtn) {
    toggleReadingBtn.addEventListener('click', toggleVideoReadingPanel);
  }
  if (closeReadingBtn) {
    closeReadingBtn.addEventListener('click', toggleVideoReadingPanel);
  }

  // Popup Quiz Actions
  document.getElementById('btn-toggle-popup-quiz').addEventListener('click', () => {
    // Open the next available uncompleted slot
    let nextSlot = -1;
    for (let i = 0; i < 6; i++) {
      if (!userProgress.popupQuizzes[`popup_slot_${i}`]) {
        nextSlot = i;
        break;
      }
    }
    if (nextSlot === -1) {
      alert("You've completed all 6 quick quizzes for today! Check your progress tracker.");
    } else {
      launchPopupQuiz(nextSlot);
    }
  });

  document.getElementById('btn-close-popup-quiz').addEventListener('click', closePopupQuizModal);
  document.getElementById('btn-popup-prev').addEventListener('click', () => navigatePopupQuiz(-1));
  document.getElementById('btn-popup-next').addEventListener('click', () => navigatePopupQuiz(1));
  document.getElementById('btn-popup-submit').addEventListener('click', submitPopupQuiz);
  
  document.getElementById('btn-close-popup-results').addEventListener('click', () => {
    document.getElementById('popup-quiz-results').style.display = 'none';
  });
  document.getElementById('btn-popup-results-close').addEventListener('click', () => {
    document.getElementById('popup-quiz-results').style.display = 'none';
  });

  // Window hash routing handler
  window.addEventListener('hashchange', handleHashRouting);

  // Search PDFs list
  const pdfsSearchInput = document.getElementById('pdfs-search-input');
  if (pdfsSearchInput) {
    pdfsSearchInput.addEventListener('input', () => {
      renderPdfLibrary(pdfsSearchInput.value);
    });
  }
  
  // Close reader button
  const closePdfReaderBtn = document.getElementById('btn-close-pdf-reader');
  if (closePdfReaderBtn) {
    closePdfReaderBtn.addEventListener('click', () => {
      document.getElementById('pdfs-library-view').style.display = 'block';
      document.getElementById('pdfs-reader-view').style.display = 'none';
    });
  }
}

// --- Dashboard Renderer ---
function renderDashboard() {
  const container = document.getElementById('calendar-days-container');
  if (!container || !studyDaysData.length) return;
  
  container.innerHTML = '';
  
  studyDaysData.forEach(day => {
    const dayCard = document.createElement('div');
    dayCard.className = 'calendar-day-card';
    dayCard.setAttribute('data-day', day.day_id);
    
    const dayKey = `day_${day.day_id}`;
    
    // Day completion check
    if (userProgress.completedDays[dayKey]) {
      dayCard.classList.add('completed');
    }

    // Determine domain category accent
    let domainClass = 'cyan';
    if (day.domain_id === 'domain_2') domainClass = 'purple';
    else if (day.domain_id === 'domain_3') domainClass = 'pink';
    else if (day.domain_id === 'domain_4') domainClass = 'amber';
    else if (day.domain_id === 'domain_5') domainClass = 'green';
    else if (!day.domain_id) domainClass = 'red'; // Review days

    if (day.day_id >= 29) {
      dayCard.classList.add('simulation-day');
    }

    // Generate Blocks HTML
    const readingKey = `${dayKey}_reading`;
    const videoKey = `${dayKey}_video`;
    const quizKey = `${dayKey}_quiz`;
    
    const rStatus = userProgress.blockProgress[readingKey] ? 'status-completed' : '';
    const vStatus = userProgress.blockProgress[videoKey] ? 'status-completed' : '';
    const qStatus = userProgress.blockProgress[quizKey] ? 'status-completed' : '';

    const blocksHTML = `
      <div class="day-blocks-row">
        <div class="day-block ${rStatus}" data-type="reading" data-day="${day.day_id}" title="${day.modules?.reading?.title || 'Reading'}">
          <svg class="block-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2zM22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          20m
        </div>
        <div class="day-block ${vStatus}" data-type="video" data-day="${day.day_id}" title="${day.modules?.video?.title || 'Video'}">
          <svg class="block-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>
          35m
        </div>
        <div class="day-block ${qStatus}" data-type="quiz" data-day="${day.day_id}" title="15 Question Quiz">
          <svg class="block-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          15q
        </div>
      </div>
    `;

    dayCard.innerHTML = `
      <div class="day-badge">DAY ${day.day_id}</div>
      <div class="day-sub text-${domainClass}">${day.sub_objective || 'Review'}</div>
      <div class="day-check-indicator"></div>
      ${day.day_id < 29 ? blocksHTML : '<div style="margin-top:8px; font-size:11px; color:var(--text-muted); text-align:center;">Review / Exam Sim</div>'}
    `;

    // Add block click listeners
    if (day.day_id < 29) {
      setTimeout(() => {
        const blocks = dayCard.querySelectorAll('.day-block');
        blocks.forEach(block => {
          block.addEventListener('click', (e) => {
            e.stopPropagation();
            const type = block.getAttribute('data-type');
            handleBlockClick(day, type);
          });
        });
      }, 0);
    }

    // Default click handler for the whole card (useful for review days)
    dayCard.addEventListener('click', (e) => {
      // Don't trigger if a block was clicked
      if (e.target.closest('.day-block')) return;
      
      if (day.day_id >= 29) {
        // Go to sim practice for review days
        document.getElementById('btn-practice').click();
        const modeSelect = document.getElementById('practice-mode');
        modeSelect.value = 'sim';
        modeSelect.dispatchEvent(new Event('change'));
      }
    });

    container.appendChild(dayCard);
  });
}

function handleBlockClick(day, type) {
  const dayKey = `day_${day.day_id}`;
  const blockKey = `${dayKey}_${type}`;
  
  // Toggle completion status if already completed
  if (userProgress.blockProgress[blockKey]) {
    if (confirm(`Mark this ${type} block as uncompleted?`)) {
      delete userProgress.blockProgress[blockKey];
      saveProgress();
    }
    return;
  }

  // Go to content
  if (type === 'reading') {
    const ref = day.modules.reading.content_ref;
    if (ref) {
      document.getElementById('btn-modules').click();
      loadReadingModule(day.sub_objective);
    }
    // Auto-mark reading as complete when opened (could be better, but simple)
    userProgress.blockProgress[blockKey] = true;
    saveProgress();
  } else if (type === 'video') {
    const ref = day.modules.video.content_ref;
    if (ref) {
      document.getElementById('btn-videos').click();
      playVideoLesson(ref, day.modules.video.title, `Sub-objective ${day.sub_objective}`, day.sub_objective);
    }
    // Auto-mark video as complete when opened
    userProgress.blockProgress[blockKey] = true;
    saveProgress();
  } else if (type === 'quiz') {
    // Launch quiz block
    startBlockQuiz(day);
  }
}

function startBlockQuiz(day) {
  const quizQuestions = day.modules.quiz.questions;
  if (!quizQuestions || quizQuestions.length === 0) {
    alert("No questions found for this quiz.");
    return;
  }
  
  // Set up quiz session state for block quiz
  quizSession.mode = 'block';
  quizSession.questions = quizQuestions;
  quizSession.userAnswers = {};
  quizSession.flaggedQuestions = {};
  quizSession.currentIndex = 0;
  quizSession.startTime = Date.now();
  quizSession.timeLeft = quizQuestions.length * 60; // 1 min per question
  quizSession.currentDayObj = day; // Keep track of the day to mark complete later

  document.getElementById('practice-setup').style.display = 'none';
  document.getElementById('practice-session').style.display = 'block';
  document.getElementById('practice-results').style.display = 'none';
  document.getElementById('practice-review').style.display = 'none';
  document.getElementById('btn-practice').click();

  // Start Timer
  document.getElementById('session-timer').textContent = formatTime(quizSession.timeLeft);
  clearInterval(quizSession.timerInterval);
  quizSession.timerInterval = setInterval(() => {
    quizSession.timeLeft--;
    document.getElementById('session-timer').textContent = formatTime(quizSession.timeLeft);
    if (quizSession.timeLeft <= 0) {
      clearInterval(quizSession.timerInterval);
      alert("Time has expired!");
      scoreExam();
    }
  }, 1000);

  renderActiveQuestion();
  renderQuestionNavGrid();
}

function renderPopupQuizTracker() {
  const container = document.getElementById('quiz-tracker-slots');
  if (!container) return;
  container.innerHTML = '';

  for (let i = 0; i < 6; i++) {
    const slot = document.createElement('div');
    slot.className = 'tracker-slot';
    slot.textContent = i + 1;
    
    const slotKey = `popup_slot_${i}`;
    const quizData = userProgress.popupQuizzes[slotKey];
    
    if (quizData && quizData.completed) {
      slot.classList.add('completed');
      slot.title = `Score: ${quizData.score}/${quizData.total}`;
    }

    // Allow user to retake or view
    slot.addEventListener('click', () => {
      launchPopupQuiz(i);
    });

    container.appendChild(slot);
  }
}

// --- Practice Engine Controller ---
function startPracticeSession() {
  const mode = document.getElementById('practice-mode').value;
  const targetDomain = document.getElementById('drill-domain').value;
  const qCount = parseInt(document.getElementById('drill-count').value);
  
  if (!questionsData.length) {
    alert("Question bank database is not fully loaded yet. Please wait a moment.");
    return;
  }

  // 1. Filter Questions
  let sessionQs = [];
  if (mode === 'sim') {
    // Under Rule #4: The full simulation runs exactly 90 questions.
    // We fetch all 90 questions parsed from Practice Exam 1.docx.
    sessionQs = questionsData.filter(q => q.source === 'docx');
    // Slice or pad to guarantee exactly 90 questions
    sessionQs = sessionQs.slice(0, 90);
    // Shuffle options inside questions to randomize review order
    sessionQs = sessionQs.map(q => {
      const options = [...q.options];
      shuffleArray(options);
      return { ...q, options };
    });
    quizSession.mode = 'sim';
    quizSession.timeLeft = 90 * 60; // 90 minutes
  } else {
    // Domain drill: Filter by selected domain name
    const matches = questionsData.filter(q => q.domain === targetDomain);
    
    if (matches.length === 0) {
      alert(`No parsed questions found in database for domain: ${targetDomain}. Defaulting to all.`);
      sessionQs = [...questionsData];
    } else {
      sessionQs = [...matches];
    }
    
    // Shuffle and slice count
    shuffleArray(sessionQs);
    sessionQs = sessionQs.slice(0, qCount);
    
    // Shuffle options
    sessionQs = sessionQs.map(q => {
      const options = [...q.options];
      shuffleArray(options);
      return { ...q, options };
    });

    quizSession.mode = 'drill';
    quizSession.timeLeft = qCount * 60; // 1 min per question
  }

  if (sessionQs.length === 0) {
    alert("Error compiling question pool. Please reload and try again.");
    return;
  }

  // Enforce Rule #11 MCQ Routing First:
  // Sort questions: multiple-choice first, simulated Performance Based Questions (PBQ) deferred to end.
  // (In our dataset, docx questions contain multiple choices, so they map to standard MCQs. 
  // If any question does not have options, or is tagged as a PBQ, we place it at the end).
  sessionQs.sort((a, b) => {
    const aIsPBQ = a.question.toLowerCase().includes("perform-based") || a.question.toLowerCase().includes("drag") || a.options.length === 0;
    const bIsPBQ = b.question.toLowerCase().includes("perform-based") || b.question.toLowerCase().includes("drag") || b.options.length === 0;
    return (aIsPBQ ? 1 : 0) - (bIsPBQ ? 1 : 0);
  });

  // 2. Reset Session State
  quizSession.questions = sessionQs;
  quizSession.userAnswers = {};
  quizSession.flaggedQuestions = {};
  quizSession.currentIndex = 0;
  quizSession.startTime = Date.now();

  // Hide Setup, Show Quiz Pane
  document.getElementById('practice-setup').style.display = 'none';
  document.getElementById('practice-session').style.display = 'block';
  document.getElementById('practice-results').style.display = 'none';
  document.getElementById('practice-review').style.display = 'none';

  // Start Timer
  document.getElementById('session-timer').textContent = formatTime(quizSession.timeLeft);
  clearInterval(quizSession.timerInterval);
  quizSession.timerInterval = setInterval(() => {
    quizSession.timeLeft--;
    document.getElementById('session-timer').textContent = formatTime(quizSession.timeLeft);
    
    if (quizSession.timeLeft <= 0) {
      clearInterval(quizSession.timerInterval);
      alert("Time has expired! Submitting your exam automatically under Rule #13 complete select policy.");
      // Auto fill unanswered to enforce Rule #13 guess policy
      quizSession.questions.forEach((_, idx) => {
        if (!quizSession.userAnswers[idx]) {
          quizSession.userAnswers[idx] = "CompTIA Guest Choice (No Penalty)";
        }
      });
      scoreExam();
    }
  }, 1000);

  // Render question index 0
  renderActiveQuestion();
  renderQuestionNavigator();
}

function renderActiveQuestion() {
  const qIndex = quizSession.currentIndex;
  const q = quizSession.questions[qIndex];
  
  document.getElementById('q-index-disp').textContent = `Question ${qIndex + 1} of ${quizSession.questions.length}`;
  document.getElementById('q-domain-disp').textContent = q.domain;
  
  // Highlight PBQs if deferred
  const isPBQ = q.question.toLowerCase().includes("perform-based") || q.question.toLowerCase().includes("drag") || q.options.length === 0;
  if (isPBQ) {
    document.getElementById('q-index-disp').textContent += " [DEFERRED PBQ]";
    document.getElementById('q-domain-disp').style.backgroundColor = "rgba(255, 171, 0, 0.1)";
    document.getElementById('q-domain-disp').style.color = "var(--color-amber)";
  } else {
    document.getElementById('q-domain-disp').style.backgroundColor = "rgba(0, 229, 255, 0.05)";
    document.getElementById('q-domain-disp').style.color = "var(--color-cyan)";
  }

  document.getElementById('q-text-disp').textContent = q.question;
  
  // Render options
  const optionsContainer = document.getElementById('q-options-container');
  optionsContainer.innerHTML = '';
  
  q.options.forEach((opt) => {
    if (!opt) return;
    const row = document.createElement('div');
    row.className = 'option-row';
    if (quizSession.userAnswers[qIndex] === opt) {
      row.classList.add('selected');
    }
    
    row.innerHTML = `
      <div class="option-dot"></div>
      <div class="option-text">${opt}</div>
    `;
    
    row.addEventListener('click', () => {
      quizSession.userAnswers[qIndex] = opt;
      // Re-draw selected state
      const siblings = optionsContainer.querySelectorAll('.option-row');
      siblings.forEach(s => s.classList.remove('selected'));
      row.classList.add('selected');
      
      // Update navigator sidebar state
      updateQuestionNavigatorBtn(qIndex);
    });
    
    optionsContainer.appendChild(row);
  });

  // Toggle Flag Button text
  const flagBtn = document.getElementById('btn-flag-question');
  if (quizSession.flaggedQuestions[qIndex]) {
    flagBtn.classList.add('btn-secondary');
    flagBtn.style.borderColor = "var(--color-amber)";
    flagBtn.querySelector('span').textContent = "Unflag Question";
  } else {
    flagBtn.style.borderColor = "";
    flagBtn.querySelector('span').textContent = "Flag Question";
  }
}

function renderQuestionNavigator() {
  const container = document.getElementById('q-nav-grid-container');
  container.innerHTML = '';
  
  quizSession.questions.forEach((_, idx) => {
    const btn = document.createElement('button');
    btn.className = 'q-nav-btn';
    btn.textContent = idx + 1;
    btn.setAttribute('data-qidx', idx);
    
    // Highlight PBQs in navigator to assist Rule #11 deferrals
    const q = quizSession.questions[idx];
    const isPBQ = q.question.toLowerCase().includes("perform-based") || q.question.toLowerCase().includes("drag") || q.options.length === 0;
    if (isPBQ) {
      btn.style.borderStyle = "dotted";
    }

    btn.addEventListener('click', () => {
      quizSession.currentIndex = idx;
      renderActiveQuestion();
      updateNavigatorActiveHighlight();
    });
    
    container.appendChild(btn);
  });
  
  updateNavigatorActiveHighlight();
  // Fill answered status
  for (let idx = 0; idx < quizSession.questions.length; idx++) {
    updateQuestionNavigatorBtn(idx);
  }
}

function updateNavigatorActiveHighlight() {
  const buttons = document.querySelectorAll('.q-nav-btn');
  buttons.forEach((btn, idx) => {
    if (idx === quizSession.currentIndex) {
      btn.classList.add('current');
    } else {
      btn.classList.remove('current');
    }
  });
}

function updateQuestionNavigatorBtn(idx) {
  const btn = document.querySelector(`.q-nav-btn[data-qidx="${idx}"]`);
  if (!btn) return;
  
  // Flag status holds precedence
  if (quizSession.flaggedQuestions[idx]) {
    btn.classList.add('flagged');
    btn.classList.remove('answered');
  } else if (quizSession.userAnswers[idx]) {
    btn.classList.add('answered');
    btn.classList.remove('flagged');
  } else {
    btn.classList.remove('answered', 'flagged');
  }
}

function navigateQuestion(dir) {
  const nextIndex = quizSession.currentIndex + dir;
  if (nextIndex >= 0 && nextIndex < quizSession.questions.length) {
    quizSession.currentIndex = nextIndex;
    renderActiveQuestion();
    updateNavigatorActiveHighlight();
  }
}

function toggleFlagActiveQuestion() {
  const idx = quizSession.currentIndex;
  quizSession.flaggedQuestions[idx] = !quizSession.flaggedQuestions[idx];
  
  // Re-render Active question & navigator button
  renderActiveQuestion();
  updateQuestionNavigatorBtn(idx);
}

// Enforce Rule #13: Complete Selection Mandate check
function submitExamHandler() {
  // Check if there are unanswered questions
  let unansweredCount = 0;
  quizSession.questions.forEach((_, idx) => {
    if (!quizSession.userAnswers[idx]) {
      unansweredCount++;
    }
  });

  if (unansweredCount > 0) {
    // Show alert blocker
    const alertModal = document.getElementById('mandate-alert');
    document.getElementById('mandate-alert-text').innerHTML = `
      You have <strong>${unansweredCount}</strong> unanswered questions!<br><br>
      CompTIA does NOT penalize incorrect answers. Leaving a blank question guaranteed 0 points.<br>
      Under <strong>Exam Hack Rule #13</strong>, you must select an answer for every single item before submitting.
    `;
    alertModal.style.display = 'flex';
  } else {
    if (confirm("Are you sure you want to submit your exam for scoring?")) {
      scoreExam();
    }
  }
}

function scoreExam() {
  clearInterval(quizSession.timerInterval);
  quizSession.timeTaken = Math.round((Date.now() - quizSession.startTime) / 1000);
  
  let correctCount = 0;
  const total = quizSession.questions.length;
  
  // Group statistics by domain
  const domainStats = {};

  quizSession.questions.forEach((q, idx) => {
    const userChoice = quizSession.userAnswers[idx];
    const isCorrect = userChoice === q.correct;
    
    if (isCorrect) correctCount++;
    
    // Group analysis
    if (!domainStats[q.domain]) {
      domainStats[q.domain] = { total: 0, correct: 0 };
    }
    domainStats[q.domain].total++;
    if (isCorrect) domainStats[q.domain].correct++;
  });

  const percentage = Math.round((correctCount / total) * 100);
  // CompTIA Passing Score: 750 / 900 (corresponds to approx 81.25%)
  const passed = percentage >= 82;

  // Block Mode Completion Handle
  if (quizSession.mode === 'block' && quizSession.currentDayObj) {
    const dayKey = `day_${quizSession.currentDayObj.day_id}`;
    const blockKey = `${dayKey}_quiz`;
    userProgress.blockProgress[blockKey] = true;
    saveProgress();
  }

  // Render Results Card UI
  document.getElementById('practice-session').style.display = 'none';
  const resultsPane = document.getElementById('practice-results');
  resultsPane.style.display = 'block';

  // Pass/Fail Classes
  const summaryCard = resultsPane.querySelector('.score-summary-card');
  if (passed) {
    summaryCard.className = 'score-summary-card passed';
    document.getElementById('result-status-text').textContent = 'EXAM PASSED (Ready for Test)';
  } else {
    summaryCard.className = 'score-summary-card failed';
    document.getElementById('result-status-text').textContent = 'EXAM FAILED (Review Weak Areas)';
  }

  document.getElementById('result-score-percent').textContent = `${percentage}%`;
  document.getElementById('result-numerical-score').textContent = `${correctCount} of ${total} Correct`;
  document.getElementById('result-time-taken').textContent = `Time taken: ${formatTime(quizSession.timeTaken)}`;

  // Animate Ring stroke-dashoffset (total length is 314)
  const offset = 314 - (314 * (percentage / 100));
  document.getElementById('result-ring-fill').style.strokeDashoffset = offset;

  // Render Domain analytics (enforcing Rule #4)
  const domainContainer = document.getElementById('result-domains-container');
  domainContainer.innerHTML = '';
  
  // Standard Domain blueprints weights for labeling
  const domainWeights = {
    "General Security Concepts": "12%",
    "Threats, Vulnerabilities, and Mitigations": "22%",
    "Security Architecture": "18%",
    "Security Operations": "28%",
    "Security Program Management and Oversight": "20%"
  };

  Object.keys(domainStats).forEach(dom => {
    const stats = domainStats[dom];
    const pct = Math.round((stats.correct / stats.total) * 100);
    const weight = domainWeights[dom] || '10%';
    
    // Set colors based on performance
    let barColor = 'var(--color-red)';
    if (pct >= 82) barColor = 'var(--color-green)';
    else if (pct >= 60) barColor = 'var(--color-amber)';

    const row = document.createElement('div');
    row.className = 'domain-perf-row';
    row.innerHTML = `
      <div class="domain-perf-header">
        <span>${dom} <span class="weight-badge">${weight} Weight</span></span>
        <span class="domain-perf-val">${stats.correct}/${stats.total} (${pct}%)</span>
      </div>
      <div class="domain-perf-bar-bg">
        <div class="domain-perf-bar-fill" style="width: ${pct}%; background-color: ${barColor};"></div>
      </div>
    `;
    domainContainer.appendChild(row);
  });
}

function showReviewPane() {
  document.getElementById('practice-results').style.display = 'none';
  const container = document.getElementById('review-questions-container');
  container.innerHTML = '';
  
  quizSession.questions.forEach((q, idx) => {
    const userChoice = quizSession.userAnswers[idx];
    const isCorrect = userChoice === q.correct;
    
    const card = document.createElement('div');
    card.className = 'review-q-card';
    
    card.innerHTML = `
      <div class="review-q-header">
        <span>Question ${idx + 1} • Sub-Objective ${q.sub_objective}</span>
        <span class="review-q-status ${isCorrect ? 'correct' : 'incorrect'}">
          ${isCorrect ? 'Correct' : 'Incorrect'}
        </span>
      </div>
      <div class="review-q-text">${q.question}</div>
      <div class="review-options">
        ${q.options.map(opt => {
          if (!opt) return '';
          let optClass = '';
          if (opt === q.correct) {
            optClass = 'actual-correct';
          }
          if (opt === userChoice) {
            optClass = isCorrect ? 'user-correct' : 'user-incorrect';
          }
          return `<div class="review-opt-row ${optClass}">${opt}</div>`;
        }).join('')}
      </div>
      <div class="review-explanation">
        <strong>Explanation Detail:</strong><br>
        ${q.explanation.replace(/\n/g, '<br>')}
      </div>
    `;
    
    container.appendChild(card);
  });
  
  document.getElementById('practice-review').style.display = 'block';
}

function endQuizUI() {
  clearInterval(quizSession.timerInterval);
  document.getElementById('practice-session').style.display = 'none';
  document.getElementById('practice-setup').style.display = 'block';
}

// --- Reading Modules View Controllers ---
function renderModulesTree(filterQuery = '') {
  const container = document.getElementById('modules-list-tree');
  if (!container || !scheduleData.length) return;
  
  container.innerHTML = '';
  
  // Group schedule assignments by Domain
  const domains = {};
  scheduleData.forEach(day => {
    // Only map learning days (days 1-28)
    if (day.day <= 28 && day.sub_objective !== "Review" && day.sub_objective !== "3.0") {
      const dom = getDayDomain(day.day);
      if (!domains[dom]) domains[dom] = [];
      
      // Prevent duplicates
      if (!domains[dom].some(item => item.sub_objective === day.sub_objective)) {
        domains[dom].push({
          sub_objective: day.sub_objective,
          name: getSubName(day.day),
          day: day.day
        });
      }
    }
  });

  Object.keys(domains).forEach(dom => {
    // Filter sub-objectives if query exists
    const filteredItems = domains[dom].filter(item => 
      item.sub_objective.toLowerCase().includes(filterQuery) || 
      item.name.toLowerCase().includes(filterQuery)
    );
    
    if (filterQuery && filteredItems.length === 0) return;

    const group = document.createElement('div');
    group.className = 'modules-tree-group';
    
    let domainColorClass = 'cyan';
    if (dom.includes("Threats")) domainColorClass = 'purple';
    else if (dom.includes("Architecture")) domainColorClass = 'pink';
    else if (dom.includes("Operations")) domainColorClass = 'amber';
    else if (dom.includes("Oversight")) domainColorClass = 'green';
    
    group.innerHTML = `
      <h4 class="text-${domainColorClass}">${dom}</h4>
      <div class="modules-tree-items"></div>
    `;
    
    const itemsContainer = group.querySelector('.modules-tree-items');
    
    filteredItems.forEach(item => {
      const btn = document.createElement('button');
      btn.className = 'module-tree-item-btn';
      btn.setAttribute('data-sub', item.sub_objective);
      btn.innerHTML = `
        <span style="display: flex; align-items: center;">
          <span class="sub-code-badge">${item.sub_objective}</span>
          <span class="module-title">${item.name}</span>
        </span>
      `;
      
      btn.addEventListener('click', () => {
        // Active highlight
        document.querySelectorAll('.module-tree-item-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        loadReadingModule(item.sub_objective);
      });
      
      itemsContainer.appendChild(btn);
    });
    
    container.appendChild(group);
  });
}

function getDayDomain(dayNum) {
  if (dayNum <= 4) return "1.0 General Security Concepts";
  if (dayNum <= 10) return "2.0 Threats, Vulnerabilities, and Mitigations";
  if (dayNum <= 15) return "3.0 Security Architecture";
  if (dayNum <= 23) return "4.0 Security Operations";
  return "5.0 Security Program Management and Oversight";
}

function getSubName(dayNum) {
  // Simple map from daily assignments helper
  const map = {
    1: "Security Controls",
    2: "Security Concepts & ZTA",
    3: "Change Management",
    4: "Cryptographic PKI",
    5: "Threat Actors",
    6: "Threat Vectors",
    7: "Code Vulnerabilities",
    8: "Malware Indicators",
    9: "Network Attacks",
    10: "Mitigations & Hardening",
    11: "Cloud Models",
    12: "Secure Infrastructure",
    13: "Data Protections",
    14: "Resiliency & Recovery",
    16: "Secure Baselines",
    17: "Asset & Vuln Management",
    18: "Monitoring & Logging",
    19: "Secure Protocols & Ports",
    20: "IAM & Credentials",
    21: "Automation Scripts",
    22: "Incident & Forensics",
    23: "Data Monitoring",
    24: "Policies & Standards",
    25: "Risk Frameworks",
    26: "Contracts & Vendor Risks",
    27: "Compliance Auditing",
    28: "Security Training"
  };
  return map[dayNum] || "Topic Review";
}

async function loadReadingModule(subCode) {
  const placeholder = document.getElementById('viewer-placeholder-text');
  const viewer = document.getElementById('viewer-content-area');
  
  placeholder.style.display = 'none';
  viewer.style.display = 'block';
  viewer.innerHTML = `<h3>Loading Module ${subCode} Content...</h3>`;
  
  try {
    const res = await fetch(`./${subCode}.md`);
    if (!res.ok) throw new Error("Module file not found");
    const markdown = await res.text();
    
    // Custom Markdown parser rendering logic
    let htmlContent = parseMarkdownToHTML(markdown);
    
    // Check if there are videos for this module and append a link/button at the top
    const subObjVideos = videosData[subCode];
    if (subObjVideos && subObjVideos.length > 0) {
      const videoLinks = subObjVideos.map(v => 
        `<button class="action-btn-primary inline-btn" style="margin: 4px; font-size: 11px; background: linear-gradient(135deg, var(--color-purple), var(--color-pink));" onclick="window.playVideoFromLink('${v.path}', '${subCode} - ${v.title}')">
           Play Video: Lesson ${v.lesson_num} - ${v.title}
         </button>`
      ).join('');
      
      htmlContent = `<div style="background: rgba(255,255,255,0.02); border: 1px solid var(--border-color); padding: 16px; border-radius: 8px; margin-bottom: 20px;">
                       <h5 style="margin-top:0; margin-bottom:8px; text-transform:uppercase; font-size:11px; color:var(--text-muted);">Related Video Lessons</h5>
                       <div style="display:flex; flex-wrap:wrap; gap:8px;">${videoLinks}</div>
                     </div>` + htmlContent;
    }
    
    viewer.innerHTML = htmlContent;
  } catch (err) {
    viewer.innerHTML = `<h3 style="color:var(--color-red)">Failed to load study guide module for sub-objective ${subCode}. Please check your files directory structure.</h3>`;
  }
}

// Simple and robust regex markdown parser
function parseMarkdownToHTML(md) {
  let htmlText = md;

  // Convert headings
  htmlText = htmlText.replace(/^# (.*?)$/gm, '<h1>$1</h1>');
  htmlText = htmlText.replace(/^## (.*?)$/gm, '<h2>$1</h2>');
  htmlText = htmlText.replace(/^### (.*?)$/gm, '<h3>$1</h3>');

  // Convert Bold Text
  htmlText = htmlText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

  // Convert math blocks (e.g. $$ formula $$)
  htmlText = htmlText.replace(/\$\$(.*?)\$\$/g, '<div style="font-family: var(--font-mono); font-size:15px; text-align:center; padding:12px; margin: 12px 0; background:rgba(0,0,0,0.2); border-radius:6px; border: 1px dashed rgba(255,255,255,0.06); font-weight:600; color: var(--color-cyan);">$1</div>');

  // Convert list items: replace groups of "- item" or "* item" with lists
  htmlText = htmlText.replace(/^\- (.*?)$/gm, '<li>$1</li>');
  htmlText = htmlText.replace(/^\* (.*?)$/gm, '<li>$1</li>');
  
  // Wrap contiguous <li> lines in <ul>
  htmlText = htmlText.replace(/(<li>.*?<\/li>)+/g, (match) => {
    return `<ul>${match}</ul>`;
  });

  // Convert remaining paragraphs (exclude lines that are already tags)
  const lines = htmlText.split('\n');
  const processedLines = lines.map(line => {
    const trimmed = line.trim();
    if (!trimmed) return '';
    if (trimmed.startsWith('<h') || trimmed.startsWith('<ul') || trimmed.startsWith('<li') || trimmed.startsWith('<div')) {
      return line;
    }
    return `<p>${line}</p>`;
  });
  
  return processedLines.join('\n');
}

// --- Flashcards deck Controller ---
function initFlashcards() {
  if (!flashcardsData.length) return;
  filterDeck();
}

function filterDeck() {
  const filterVal = document.getElementById('flashcards-filter').value;
  
  if (filterVal === 'acronym') {
    // Acronyms usually have short uppercase front text
    filteredFlashcards = flashcardsData.filter(card => {
      const frontClean = card.front.replace(/\(.*\)/g, '').trim();
      // check if word is fully uppercase and short or matches question-less criteria
      return !card.front.includes("?") && (frontClean.length <= 10 && frontClean === frontClean.toUpperCase());
    });
  } else if (filterVal === 'term') {
    // Definition questions/terms
    filteredFlashcards = flashcardsData.filter(card => {
      const frontClean = card.front.replace(/\(.*\)/g, '').trim();
      return card.front.includes("?") || !(frontClean.length <= 10 && frontClean === frontClean.toUpperCase());
    });
  } else {
    filteredFlashcards = [...flashcardsData];
  }

  if (filteredFlashcards.length === 0) {
    filteredFlashcards = [{ front: "No cards matched.", back: "Change your filter option." }];
  }

  flashcardIndex = 0;
  renderFlashcard();
}

function shuffleDeck() {
  shuffleArray(filteredFlashcards);
}

function renderFlashcard() {
  isFlipped = false;
  document.getElementById('flashcard-container').classList.remove('flipped');

  const card = filteredFlashcards[flashcardIndex];
  
  document.getElementById('card-front-text').textContent = card.front;
  document.getElementById('card-back-text').textContent = card.back;
  
  // Update deck index details
  document.getElementById('deck-progress-text').textContent = `Card ${flashcardIndex + 1} of ${filteredFlashcards.length}`;
  const pct = ((flashcardIndex + 1) / filteredFlashcards.length) * 100;
  document.getElementById('deck-progress-fill').style.width = `${pct}%`;
}

function navigateCard(dir) {
  const nextIdx = flashcardIndex + dir;
  if (nextIdx >= 0 && nextIdx < filteredFlashcards.length) {
    flashcardIndex = nextIdx;
    renderFlashcard();
  }
}

// --- Helper Utilities ---
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

function formatTime(totalSecs) {
  const mins = Math.floor(totalSecs / 60);
  const secs = totalSecs % 60;
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

// --- Videos View Controllers ---
window.playVideoFromLink = (path, title) => {
  playVideoLesson(path, title, `Video lesson for Objective.`);
};

function renderVideosTree(filterQuery = '') {
  const container = document.getElementById('videos-list-tree');
  if (!container || !scheduleData.length) return;
  
  container.innerHTML = '';
  
  // Group lessons by Domain
  const domains = {};
  scheduleData.forEach(day => {
    if (day.day <= 28 && day.sub_objective !== "Review" && day.sub_objective !== "3.0") {
      const dom = getDayDomain(day.day);
      if (!domains[dom]) domains[dom] = [];
      
      if (!domains[dom].some(item => item.sub_objective === day.sub_objective)) {
        domains[dom].push({
          sub_objective: day.sub_objective,
          name: getSubName(day.day),
          day: day.day
        });
      }
    }
  });

  Object.keys(domains).forEach(dom => {
    const group = document.createElement('div');
    group.className = 'modules-tree-group';
    
    let domainColorClass = 'cyan';
    if (dom.includes("Threats")) domainColorClass = 'purple';
    else if (dom.includes("Architecture")) domainColorClass = 'pink';
    else if (dom.includes("Operations")) domainColorClass = 'amber';
    else if (dom.includes("Oversight")) domainColorClass = 'green';
    
    group.innerHTML = `
      <h4 class="text-${domainColorClass}">${dom}</h4>
      <div class="videos-tree-items" style="display:flex; flex-direction:column; gap:4px;"></div>
    `;
    
    const itemsContainer = group.querySelector('.videos-tree-items');
    let hasMatchingLessons = false;
    
    domains[dom].forEach(item => {
      const subObjVideos = videosData[item.sub_objective] || [];
      const filteredVideos = subObjVideos.filter(v => 
        v.title.toLowerCase().includes(filterQuery) || 
        item.sub_objective.toLowerCase().includes(filterQuery) ||
        item.name.toLowerCase().includes(filterQuery)
      );
      
      if (filteredVideos.length > 0) {
        hasMatchingLessons = true;
        
        filteredVideos.forEach(v => {
          const btn = document.createElement('button');
          btn.className = 'module-tree-item-btn';
          btn.setAttribute('data-video-path', v.path);
          btn.innerHTML = `
            <span style="display: flex; align-items: center; text-align: left;">
              <span class="sub-code-badge" style="background-color: rgba(179, 136, 255, 0.15); color: var(--color-purple);">${item.sub_objective} L${v.lesson_num}</span>
              <span class="module-title">${v.title}</span>
            </span>
          `;
          
          btn.addEventListener('click', () => {
            document.querySelectorAll('.module-tree-item-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            playVideoLesson(v.path, `${item.sub_objective} - ${v.title}`, `Streaming: Lesson ${v.lesson_num} for Objective ${item.sub_objective} - ${item.name}.`, item.sub_objective);
          });
          
          itemsContainer.appendChild(btn);
        });
      }
    });
    
    if (hasMatchingLessons) {
      container.appendChild(group);
    }
  });
}

function playVideoLesson(videoPath, title, desc, subObjective = null) {
  // Switch to videos tab if not active
  const videosBtn = document.getElementById('btn-videos');
  if (videosBtn && !videosBtn.classList.contains('active')) {
    videosBtn.click();
  }
  
  const placeholder = document.getElementById('video-placeholder-text');
  const playerContainer = document.getElementById('video-player-container');
  const videoPlayer = document.getElementById('video-player-element');
  
  placeholder.style.display = 'none';
  playerContainer.style.display = 'flex';
  
  document.getElementById('video-active-title').textContent = title;
  document.getElementById('video-active-desc').textContent = desc;
  
  // Set video source and play
  videoPlayer.src = videoPath;
  videoPlayer.load();
  
  // Catch browser auto-play blockers
  videoPlayer.play().catch(err => {
    console.log("Auto-play blocked by browser. User gesture needed to start audio/video streams.");
  });

  // Highlight active tree item matching this video path
  document.querySelectorAll('.module-tree-item-btn').forEach(b => {
    if (b.getAttribute('data-video-path') === videoPath) {
      b.classList.add('active');
    } else {
      b.classList.remove('active');
    }
  });

  // Prepare reading context for split-screen
  currentVideoSubObjective = subObjective;
  
  // If reading panel is open, refresh it
  const readingPanel = document.getElementById('video-reading-panel');
  if (readingPanel.style.display !== 'none') {
    loadSplitScreenReading(subObjective);
  }
}

function toggleVideoReadingPanel() {
  const container = document.getElementById('video-player-container');
  const readingPanel = document.getElementById('video-reading-panel');
  const isActive = container.classList.contains('reading-active');
  
  if (isActive) {
    // Close it
    container.classList.remove('reading-active');
    readingPanel.style.display = 'none';
  } else {
    // Open it
    container.classList.add('reading-active');
    readingPanel.style.display = 'flex';
    loadSplitScreenReading(currentVideoSubObjective);
  }
}

async function loadSplitScreenReading(subObj) {
  const contentDiv = document.getElementById('video-reading-content');
  if (!subObj) {
    contentDiv.innerHTML = '<p style="color: var(--text-muted);">No reading material linked to this video lesson.</p>';
    return;
  }
  
  contentDiv.innerHTML = '<em>Loading reading material...</em>';
  try {
    const res = await fetch(`./${subObj}.md`);
    if (!res.ok) {
      contentDiv.innerHTML = '<p style="color: var(--text-muted);">Reading material not available.</p>';
      return;
    }
    const md = await res.text();
    contentDiv.innerHTML = parseMarkdownToHTML(md);
  } catch (err) {
    contentDiv.innerHTML = '<p style="color: var(--color-red);">Error loading material.</p>';
  }
}

// --- PDFs & Docs Router and Render Controllers ---
function handleHashRouting() {
  const hash = location.hash.toLowerCase();
  
  if (hash === '#pdfs' || hash === '#docs') {
    // Deactivate all sidebar buttons
    document.querySelectorAll('.menu-btn').forEach(btn => btn.classList.remove('active'));
    
    // Deactivate all panes
    document.querySelectorAll('.pane').forEach(pane => pane.classList.remove('active'));
    
    // Activate PDF pane
    const pdfPane = document.getElementById('pane-pdfs');
    if (pdfPane) {
      pdfPane.classList.add('active');
    }
    
    // Pause any running videos when switching away
    const player = document.getElementById('video-player-element');
    if (player) {
      player.pause();
    }
    
    // Reset reader view back to library grid
    document.getElementById('pdfs-library-view').style.display = 'block';
    document.getElementById('pdfs-reader-view').style.display = 'none';
    
    // Render PDFs library
    renderPdfLibrary();
  } else if (hash) {
    const paneId = hash.substring(1);
    const btn = document.querySelector(`.menu-btn[data-pane="${paneId}"]`);
    if (btn && !btn.classList.contains('active')) {
      btn.click();
    }
  }
}

function renderPdfLibrary(filterQuery = '') {
  const gridContainer = document.getElementById('pdfs-grid-container');
  if (!gridContainer) return;
  
  gridContainer.innerHTML = '';
  
  if (!pdfsData.length) {
    gridContainer.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">
        <p>No study guide PDF documents have been processed yet.</p>
        <p style="font-size: 12px; margin-top: 8px;">Run the asset processing script in the workspace to generate the PDF database.</p>
      </div>
    `;
    return;
  }
  
  const query = filterQuery.toLowerCase().trim();
  const filteredPdfs = pdfsData.filter(pdf => 
    pdf.title.toLowerCase().includes(query) || 
    pdf.pdf_path.toLowerCase().includes(query)
  );
  
  if (filteredPdfs.length === 0) {
    gridContainer.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">
        <p>No PDF files matched your search "${filterQuery}".</p>
      </div>
    `;
    return;
  }
  
  filteredPdfs.forEach(pdf => {
    const card = document.createElement('div');
    card.className = 'pdf-card';
    
    let docType = "Study Reference";
    if (pdf.pdf_path.toLowerCase().includes("objectives")) docType = "Exam Objectives Blueprint";
    else if (pdf.pdf_path.toLowerCase().includes("notes") || pdf.pdf_path.toLowerCase().includes("cheat")) docType = "High-Yield Notes";
    else if (pdf.pdf_path.toLowerCase().includes("practice")) docType = "Practice Exam Book";
    else if (pdf.pdf_path.toLowerCase().includes("slides")) docType = "Presentation Slides PDF";
    
    card.innerHTML = `
      <div>
        <div class="pdf-card-title">${pdf.title}</div>
        <div class="pdf-card-meta">${docType}</div>
      </div>
      <div class="pdf-card-actions">
        <button class="action-btn-primary inline-btn btn-read-md" data-md="${pdf.md_path}" data-title="${pdf.title}">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2zM22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          Read Markdown
        </button>
        <a href="${pdf.pdf_path}" target="_blank" class="btn-download btn-secondary inline-btn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
          Download PDF
        </a>
      </div>
    `;
    
    card.querySelector('.btn-read-md').addEventListener('click', (e) => {
      const mdPath = e.currentTarget.getAttribute('data-md');
      const title = e.currentTarget.getAttribute('data-title');
      openPdfReader(mdPath, title);
    });
    
    container.appendChild(card);
  });
}

// ════════════════════════════════════════════════════════════════
// DOMAINS DEEP DIVE LOGIC
// ════════════════════════════════════════════════════════════════

function renderDomainDeepDive(domainId) {
  const domain = domainsData[domainId];
  if (!domain) return;
  
  // Highlight tab
  document.querySelectorAll('#domain-selector-bar .domain-tab').forEach(t => {
    if (t.getAttribute('data-domain') === domainId) t.classList.add('active');
    else t.classList.remove('active');
  });

  const container = document.getElementById('domain-deep-content');
  container.innerHTML = '';
  
  const colorMap = {
    'domain_1': 'cyan',
    'domain_2': 'purple',
    'domain_3': 'pink',
    'domain_4': 'amber',
    'domain_5': 'green'
  };
  const dColor = colorMap[domainId];

  // Title section
  container.innerHTML += `
    <div style="padding-bottom: 12px; border-bottom: 1px solid var(--border-color);">
      <h2 style="color: var(--color-${dColor}); margin-bottom: 8px;">${domain.title}</h2>
      <p style="color: var(--text-muted); font-size: 14px;">${domain.description}</p>
    </div>
  `;

  // 1. Videos Section
  let videosHTML = '';
  domain.videos.forEach(v => {
    videosHTML += `
      <div class="domain-item-card" onclick="document.getElementById('btn-videos').click(); playVideoLesson('${v.url}', '${v.sub_objective} - ${v.title}', 'Lesson ${v.lesson_num}', '${v.sub_objective}')">
        <div class="item-title">${v.title}</div>
        <div class="item-meta">Sub-Objective ${v.sub_objective} • Lesson ${v.lesson_num}</div>
      </div>
    `;
  });
  
  container.innerHTML += `
    <div class="domain-section sec-videos">
      <div class="domain-section-header">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>
        <h3>Video Lectures</h3>
        <span class="section-count">${domain.videos.length}</span>
      </div>
      <div class="domain-items-grid">${videosHTML}</div>
    </div>
  `;

  // 2. Readings Section
  let readingsHTML = '';
  domain.readings.forEach(r => {
    readingsHTML += `
      <div class="domain-item-card" onclick="document.getElementById('btn-modules').click(); loadReadingModule('${r.sub_objective}')">
        <div class="item-title">${r.title}</div>
        <div class="item-meta">${r.sub_objective === 'all' ? 'Comprehensive Reference' : 'Specific Sub-Objective'}</div>
      </div>
    `;
  });

  container.innerHTML += `
    <div class="domain-section sec-readings">
      <div class="domain-section-header">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2zM22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
        <h3>Reading Materials</h3>
        <span class="section-count">${domain.readings.length}</span>
      </div>
      <div class="domain-items-grid">${readingsHTML}</div>
    </div>
  `;

  // 3. Flashcards Section (Accordions)
  let flashcardsHTML = '';
  domain.flashcards.forEach((fc, idx) => {
    flashcardsHTML += `
      <div class="fc-accordion">
        <div class="fc-accordion-header" onclick="this.parentElement.classList.toggle('open')">
          <span>Q: ${fc.question}</span>
          <svg class="fc-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
        </div>
        <div class="fc-accordion-body">
          <p><strong>A:</strong> ${fc.answer}</p>
        </div>
      </div>
    `;
  });

  container.innerHTML += `
    <div class="domain-section sec-flashcards">
      <div class="domain-section-header">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M21 12H3M12 3v18"/></svg>
        <h3>Flashcards</h3>
        <span class="section-count">${domain.flashcards.length}</span>
      </div>
      <div style="display:flex; flex-direction:column; gap:10px; max-height:400px; overflow-y:auto; padding-right:8px;">${flashcardsHTML}</div>
    </div>
  `;

  // 4. Quizzes Section
  let quizzesHTML = '';
  domain.quizzes.forEach((q, idx) => {
    quizzesHTML += `
      <div class="domain-item-card" data-quiz-idx="${idx}">
        <div class="item-title">${q.title}</div>
        <div class="item-meta">${q.questions_count} Questions</div>
      </div>
    `;
  });

  container.innerHTML += `
    <div class="domain-section sec-quizzes">
      <div class="domain-section-header">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        <h3>Practice Quizzes</h3>
        <span class="section-count">${domain.quizzes.length}</span>
      </div>
      <div class="domain-items-grid" id="domain-quizzes-grid">${quizzesHTML}</div>
    </div>
  `;

  // Bind quiz buttons
  setTimeout(() => {
    document.querySelectorAll('#domain-quizzes-grid .domain-item-card').forEach(card => {
      card.addEventListener('click', () => {
        const qIdx = parseInt(card.getAttribute('data-quiz-idx'));
        startDomainQuiz(domain, qIdx);
      });
    });
  }, 0);
}

function startDomainQuiz(domain, quizIdx) {
  const quiz = domain.quizzes[quizIdx];
  if (!quiz) return;
  
  quizSession.mode = 'block';
  quizSession.questions = quiz.questions;
  quizSession.userAnswers = {};
  quizSession.flaggedQuestions = {};
  quizSession.currentIndex = 0;
  quizSession.startTime = Date.now();
  quizSession.timeLeft = quiz.questions.length * 60; // 1 min per question

  document.getElementById('practice-setup').style.display = 'none';
  document.getElementById('practice-session').style.display = 'block';
  document.getElementById('practice-results').style.display = 'none';
  document.getElementById('practice-review').style.display = 'none';
  document.getElementById('btn-practice').click();

  // Start Timer
  document.getElementById('session-timer').textContent = formatTime(quizSession.timeLeft);
  clearInterval(quizSession.timerInterval);
  quizSession.timerInterval = setInterval(() => {
    quizSession.timeLeft--;
    document.getElementById('session-timer').textContent = formatTime(quizSession.timeLeft);
    if (quizSession.timeLeft <= 0) {
      clearInterval(quizSession.timerInterval);
      alert("Time has expired!");
      scoreExam();
    }
  }, 1000);

  renderActiveQuestion();
  renderQuestionNavGrid();
}

// ════════════════════════════════════════════════════════════════
// EXAM OBJECTIVES BROWSER
// ════════════════════════════════════════════════════════════════

function renderObjectivesBrowser(query = '', domainFilter = 'all') {
  const container = document.getElementById('objectives-list');
  if (!container || !examObjectivesData.length) return;
  
  container.innerHTML = '';
  const lq = query.toLowerCase();

  let filtered = examObjectivesData;
  if (domainFilter !== 'all') {
    filtered = filtered.filter(o => o.domain_id === domainFilter);
  }

  if (query) {
    filtered = filtered.filter(o => {
      if (o.code.includes(lq) || o.title.toLowerCase().includes(lq)) return true;
      if (o.bullets.some(b => b.toLowerCase().includes(lq))) return true;
      return false;
    });
  }

  filtered.forEach(obj => {
    let bulletsHTML = '';
    obj.bullets.forEach(b => {
      bulletsHTML += `<div class="obj-bullet">${b}</div>`;
    });

    const card = document.createElement('div');
    card.className = 'objective-card';
    card.innerHTML = `
      <div class="objective-card-header" onclick="this.parentElement.classList.toggle('open')">
        <span class="obj-code ${obj.domain_id}">${obj.code}</span>
        <span class="obj-title-text">${obj.title}</span>
        <svg class="obj-expand-arrow" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="objective-card-body">
        <div class="obj-bullets">
          ${bulletsHTML}
        </div>
      </div>
    `;
    // If searching, keep them open by default
    if (query) card.classList.add('open');
    container.appendChild(card);
  });

  if (filtered.length === 0) {
    container.innerHTML = `<p style="color:var(--text-muted); padding: 20px;">No exam objectives match your search.</p>`;
  }
}

// ════════════════════════════════════════════════════════════════
// POPUP QUIZ MODAL LOGIC
// ════════════════════════════════════════════════════════════════

function launchPopupQuiz(slotIndex) {
  // 10 random questions
  const pool = [...questionsData];
  shuffleArray(pool);
  const qs = pool.slice(0, 10).map(q => {
    const opts = [...q.options];
    shuffleArray(opts);
    return { ...q, options: opts };
  });

  popupQuizState.slotIndex = slotIndex;
  popupQuizState.questions = qs;
  popupQuizState.userAnswers = {};
  popupQuizState.currentIndex = 0;

  renderPopupQuizQuestion();
  document.getElementById('popup-quiz-modal').style.display = 'flex';
}

function closePopupQuizModal() {
  document.getElementById('popup-quiz-modal').style.display = 'none';
}

function renderPopupQuizQuestion() {
  const q = popupQuizState.questions[popupQuizState.currentIndex];
  
  document.getElementById('popup-quiz-progress').textContent = `Question ${popupQuizState.currentIndex + 1} of ${popupQuizState.questions.length}`;
  document.getElementById('popup-q-text').textContent = q.question;
  
  const optsContainer = document.getElementById('popup-q-options');
  optsContainer.innerHTML = '';
  
  q.options.forEach((optText, idx) => {
    const optDiv = document.createElement('div');
    optDiv.className = 'popup-opt';
    if (popupQuizState.userAnswers[popupQuizState.currentIndex] === optText) {
      optDiv.classList.add('selected');
    }
    
    optDiv.innerHTML = `
      <div class="opt-dot"></div>
      <div class="opt-text">${optText}</div>
    `;
    
    optDiv.addEventListener('click', () => {
      popupQuizState.userAnswers[popupQuizState.currentIndex] = optText;
      renderPopupQuizQuestion();
    });
    
    optsContainer.appendChild(optDiv);
  });

  // Buttons
  document.getElementById('btn-popup-prev').disabled = popupQuizState.currentIndex === 0;
  
  if (popupQuizState.currentIndex === popupQuizState.questions.length - 1) {
    document.getElementById('btn-popup-next').style.display = 'none';
    document.getElementById('btn-popup-submit').style.display = 'block';
  } else {
    document.getElementById('btn-popup-next').style.display = 'block';
    document.getElementById('btn-popup-submit').style.display = 'none';
  }
}

function navigatePopupQuiz(dir) {
  const nextIdx = popupQuizState.currentIndex + dir;
  if (nextIdx >= 0 && nextIdx < popupQuizState.questions.length) {
    popupQuizState.currentIndex = nextIdx;
    renderPopupQuizQuestion();
  }
}

function submitPopupQuiz() {
  // Check if all answered
  const total = popupQuizState.questions.length;
  let answered = Object.keys(popupQuizState.userAnswers).length;
  if (answered < total) {
    if (!confirm(`You have ${total - answered} unanswered questions. Submit anyway?`)) return;
  }

  let score = 0;
  popupQuizState.questions.forEach((q, idx) => {
    if (popupQuizState.userAnswers[idx] === q.answer) {
      score++;
    }
  });

  // Save progress
  const slotKey = `popup_slot_${popupQuizState.slotIndex}`;
  userProgress.popupQuizzes[slotKey] = {
    score: score,
    total: total,
    completed: true
  };
  saveProgress();

  // Show Results
  document.getElementById('popup-quiz-modal').style.display = 'none';
  const resultsModal = document.getElementById('popup-quiz-results');
  document.getElementById('popup-score-display').textContent = `${score}/${total}`;
  
  let msg = "Great job!";
  if (score === total) msg = "Perfect score! Outstanding.";
  else if (score < total / 2) msg = "Keep reviewing your materials, you'll get it.";
  document.getElementById('popup-score-msg').textContent = msg;

  resultsModal.style.display = 'flex';
}

async function openPdfReader(mdPath, title) {
  const libraryView = document.getElementById('pdfs-library-view');
  const readerView = document.getElementById('pdfs-reader-view');
  const contentArea = document.getElementById('pdf-reader-content-area');
  
  if (!libraryView || !readerView || !contentArea) return;
  
  libraryView.style.display = 'none';
  readerView.style.display = 'flex';
  contentArea.innerHTML = `<h3>Loading Markdown document...</h3>`;
  
  try {
    const res = await fetch(mdPath);
    if (!res.ok) throw new Error("Document not found");
    const markdown = await res.text();
    
    const htmlContent = `
      <h1 style="color: var(--color-cyan); margin-bottom: 24px; border-bottom: 1px solid var(--border-color); padding-bottom: 12px;">${title}</h1>
      <div style="font-size: 14.5px; line-height: 1.7; color: var(--text-main);">
        ${parseMarkdownToHTML(markdown)}
      </div>
    `;
    contentArea.innerHTML = htmlContent;
    contentArea.scrollTop = 0;
  } catch (err) {
    contentArea.innerHTML = `<h3 style="color:var(--color-red)">Failed to load Markdown companion document. The conversion might still be in progress.</h3>`;
  }
}


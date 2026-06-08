// Antigravity Security+ (SY0-701) Study Portal App Logic

// --- Global State ---
let scheduleData = [];
let questionsData = [];
let flashcardsData = [];
let filteredFlashcards = [];

// Persistent user progress schema in localStorage
let userProgress = {
  checkedItems: {}, // key: "dayX_itemY", value: true/false
  completedDays: {}, // key: "dayX", value: true/false
};

// Quiz Session State
let quizSession = {
  mode: 'sim', // 'sim' or 'drill'
  questions: [], // active questions list
  userAnswers: {}, // key: qIndex, value: selectedOptionText
  flaggedQuestions: {}, // key: qIndex, value: true/false
  currentIndex: 0,
  timeLeft: 0, // in seconds
  timerInterval: null,
  startTime: 0,
  timeTaken: 0
};

// Flashcards State
let flashcardIndex = 0;
let isFlipped = false;

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
  if (!scheduleData.length) return;
  
  let completedCount = 0;
  scheduleData.forEach(day => {
    const dayKey = `day_${day.day}`;
    // Check if day is marked completed
    let allChecked = true;
    day.checklist_payload.forEach((item, idx) => {
      const itemKey = `${dayKey}_item_${idx}`;
      if (!userProgress.checkedItems[itemKey]) {
        allChecked = false;
      }
    });
    
    if (day.checklist_payload.length > 0 && allChecked) {
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
  scheduleData.forEach(day => {
    const card = document.querySelector(`.calendar-day-card[data-day="${day.day}"]`);
    if (card) {
      const dayKey = `day_${day.day}`;
      if (userProgress.completedDays[dayKey]) {
        card.classList.add('completed');
      } else {
        card.classList.remove('completed');
      }
    }
  });
}

// --- Routing Engine ---
function initRouter() {
  const menuButtons = document.querySelectorAll('.menu-btn');
  const panes = document.querySelectorAll('.pane');

  menuButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const paneId = btn.getAttribute('data-pane');
      
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
      if (paneId === 'dashboard') {
        renderDashboard();
      } else if (paneId === 'modules') {
        renderModulesTree();
      } else if (paneId === 'flashcards') {
        initFlashcards();
      }
    });
  });
}

// --- Fetch Data Assets ---
async function loadData() {
  try {
    const [scheduleRes, questionsRes, flashcardsRes] = await Promise.all([
      fetch('./schedule.json'),
      fetch('./questions.json'),
      fetch('./flashcards.json')
    ]);

    scheduleData = await scheduleRes.json();
    questionsData = await questionsRes.json();
    flashcardsData = (await flashcardsRes.json()).cards;

    renderDashboard();
    renderModulesTree();
    updateOverallProgress();
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
}

// --- Dashboard Renderer ---
function renderDashboard() {
  const container = document.getElementById('calendar-days-container');
  if (!container || !scheduleData.length) return;
  
  container.innerHTML = '';
  
  scheduleData.forEach(day => {
    const dayCard = document.createElement('div');
    dayCard.className = 'calendar-day-card';
    dayCard.setAttribute('data-day', day.day);
    
    // Highlights if simulation day (days 29-34)
    if (day.day >= 29) {
      dayCard.classList.add('simulation-day');
    }

    const dayKey = `day_${day.day}`;
    if (userProgress.completedDays[dayKey]) {
      dayCard.classList.add('completed');
    }

    // Determine domain category accent
    let domainClass = 'cyan';
    if (day.day >= 5 && day.day <= 10) domainClass = 'purple';
    else if (day.day >= 11 && day.day <= 15) domainClass = 'pink';
    else if (day.day >= 16 && day.day <= 23) domainClass = 'amber';
    else if (day.day >= 24 && day.day <= 28) domainClass = 'green';
    else if (day.day >= 29) domainClass = 'red';

    dayCard.innerHTML = `
      <div class="day-badge">DAY ${day.day}</div>
      <div class="day-sub text-${domainClass}">${day.sub_objective}</div>
      <div class="day-check-indicator"></div>
    `;

    dayCard.addEventListener('click', () => openDayModal(day));
    container.appendChild(dayCard);
  });
}

function openDayModal(day) {
  const modal = document.getElementById('day-modal');
  document.getElementById('modal-day-title').textContent = `Day ${day.day}: ${day.date}`;
  document.getElementById('modal-t1-desc').textContent = day.track_1.description;
  document.getElementById('modal-t2-desc').textContent = day.track_2.description;
  
  // Track 1 launch configuration
  const startT1Btn = document.getElementById('modal-btn-start-t1');
  startT1Btn.onclick = () => {
    modal.style.display = 'none';
    
    // Switch to practice pane
    document.getElementById('btn-practice').click();
    
    // Set up practice mode based on day
    const modeSelect = document.getElementById('practice-mode');
    const domainSelect = document.getElementById('drill-domain');
    const countSelect = document.getElementById('drill-count');
    
    if (day.day >= 29) {
      modeSelect.value = 'sim';
      modeSelect.dispatchEvent(new Event('change'));
    } else {
      modeSelect.value = 'drill';
      modeSelect.dispatchEvent(new Event('change'));
      // select target domain
      const domains = [
        "General Security Concepts", 
        "Threats, Vulnerabilities, and Mitigations", 
        "Security Architecture", 
        "Security Operations", 
        "Security Program Management and Oversight"
      ];
      // Select domain matching the current sub-objective category
      let targetDomain = domains[0];
      if (day.day >= 5 && day.day <= 10) targetDomain = domains[1];
      else if (day.day >= 11 && day.day <= 15) targetDomain = domains[2];
      else if (day.day >= 16 && day.day <= 23) targetDomain = domains[3];
      else if (day.day >= 24 && day.day <= 28) targetDomain = domains[4];
      
      domainSelect.value = targetDomain;
      countSelect.value = "15";
    }
  };

  // Track 2 launch configuration
  const viewT2Btn = document.getElementById('modal-btn-view-t2');
  if (day.day >= 29) {
    viewT2Btn.textContent = "Open Flashcards Deck";
    viewT2Btn.onclick = () => {
      modal.style.display = 'none';
      document.getElementById('btn-flashcards').click();
    };
  } else {
    viewT2Btn.textContent = "Open Reading Module";
    viewT2Btn.onclick = () => {
      modal.style.display = 'none';
      document.getElementById('btn-modules').click();
      
      // Load specific sub-objective
      loadReadingModule(day.sub_objective);
    };
  }

  // Render Checklists
  const checklistContainer = document.getElementById('modal-checklist-items-container');
  checklistContainer.innerHTML = '';
  
  day.checklist_payload.forEach((item, idx) => {
    const itemKey = `day_${day.day}_item_${idx}`;
    const row = document.createElement('label');
    row.className = 'checklist-row';
    
    const isChecked = userProgress.checkedItems[itemKey] ? 'checked' : '';
    
    row.innerHTML = `
      <input type="checkbox" id="${itemKey}" ${isChecked}>
      <span>${item}</span>
    `;
    
    const checkbox = row.querySelector('input');
    checkbox.addEventListener('change', () => {
      userProgress.checkedItems[itemKey] = checkbox.checked;
      saveProgress();
    });
    
    checklistContainer.appendChild(row);
  });

  modal.style.display = 'flex';
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
    const res = await fetch(`./modules/${subCode}.md`);
    if (!res.ok) throw new Error("Module file not found");
    const markdown = await res.text();
    
    // Custom Markdown parser rendering logic
    viewer.innerHTML = parseMarkdownToHTML(markdown);
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

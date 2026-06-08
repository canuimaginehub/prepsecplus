<?php
// contact.php - Secure mail sender for Ferozo Hosting
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type");
header("Content-Type: application/json; charset=UTF-8");

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    http_response_code(405);
    echo json_encode(["success" => false, "message" => "Method Not Allowed"]);
    exit;
}

// Get POST data (supporting JSON or Form Data)
$input = json_decode(file_get_contents("php://input"), true);
if (!$input) {
    $input = $_POST;
}

// Basic Sanitization
$name = filter_var($input["name"] ?? "", FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$email = filter_var($input["email"] ?? "", FILTER_VALIDATE_EMAIL);
$subject = filter_var($input["subject"] ?? "New Contact Message - SecPlus", FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$message = filter_var($input["message"] ?? "", FILTER_SANITIZE_FULL_SPECIAL_CHARS);

if (empty($name) || !$email || empty($message)) {
    http_response_code(400);
    echo json_encode(["success" => false, "message" => "Please fill out all fields correctly. Valid email is required."]);
    exit;
}

// Recipient email (administrators or target address)
$to = "norberto@canuimagine.co";

// Headers to prevent mail header injection and formatting email as HTML
$email_headers = "MIME-Version: 1.0\r\n";
$email_headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$email_headers .= "From: SecPlus Portal <noreply@canuimagine.co>\r\n";
$email_headers .= "Reply-To: $name <$email>\r\n";
$email_headers .= "X-Mailer: PHP/" . phpversion();

// Build Email HTML Content
$email_content = "
<html>
<head>
  <title>" . htmlspecialchars($subject) . "</title>
</head>
<body style='font-family: Arial, sans-serif; line-height: 1.6; color: #333;'>
  <div style='max-width: 600px; margin: 20px auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px; background-color: #f9f9f9;'>
    <h2 style='color: #2b6cb0; border-bottom: 2px solid #2b6cb0; padding-bottom: 10px;'>New message from SecPlus Study Portal</h2>
    <p><strong>Name:</strong> " . htmlspecialchars($name) . "</p>
    <p><strong>Email:</strong> <a href='mailto:" . htmlspecialchars($email) . "'>" . htmlspecialchars($email) . "</a></p>
    <p><strong>Subject:</strong> " . htmlspecialchars($subject) . "</p>
    <div style='margin-top: 20px; padding: 15px; background-color: #fff; border-left: 4px solid #2b6cb0; border-radius: 4px;'>
      <p style='margin: 0;'><strong>Message:</strong></p>
      <p style='margin: 10px 0 0 0; white-space: pre-wrap;'>" . nl2br(htmlspecialchars($message)) . "</p>
    </div>
  </div>
</body>
</html>
";

if (mail($to, $subject, $email_content, $email_headers)) {
    http_response_code(200);
    echo json_encode(["success" => true, "message" => "Your message has been sent successfully."]);
} else {
    http_response_code(500);
    echo json_encode(["success" => false, "message" => "An error occurred while sending the email. Please try again later."]);
}
?>

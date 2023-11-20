<?php

use PHPMailer\PHPMailer\PHPMailer;
USE PHPMailer\PHPMailer\Exception;

require 'path/to/PHPMailer/src/Exception.php';
require 'path/to/PHPMailer/src/PHPMailer.php';
require 'path/to/PHPMailer/src/SMTP.php';

if(isset($_POST['send'])) {
    $name = htmlentities($_POST['name']);
    $email = htmlentities($_POST['email']);
    $subject = htmlentities($_POST['subject']);
    $message = htmlentities($_POST['message']);

// Create a new PHPMailer instance
$mail = new PHPMailer(true);

// Enable SMTP debugging (optional)
$mail->SMTPDebug = 2;

// Set the hostname of the mail server
$mail->Host = 'smtp.gmail.com'; // Use Gmail SMTP server

// Set the SMTP port number - 587 for TLS, 465 for SSL
$mail->Port = 587;

// Set the encryption system to use - tls
$mail->SMTPSecure = 'tls';

// SMTP authentication
$mail->SMTPAuth = true;

// Your Gmail username (full email address) and password
$mail->Username = 'ctubuddycolleague@gmail.com'; // Replace with your Gmail email address
$mail->Password = 'teyltxoivrwhdrbm'; // Replace with your Gmail password

// Set the 'from' email address and name
$mail->setFrom('your-gmail@gmail.com', 'Your Name');

// Add the recipient email address
$mail->addAddress('ctubuddycolleague@gmail.com', 'Philip');

// Email subject and body
$mail->Subject = 'Test Email';
$mail->Body = 'This is a test email sent via Gmail SMTP';

// Send the email
if ($mail->send()) {
    echo 'Email sent successfully!';
} else {
    echo 'Email sending failed: ' . $mail->ErrorInfo;
}
}
?>

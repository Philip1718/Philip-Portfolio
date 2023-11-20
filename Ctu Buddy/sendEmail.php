<?php
use PHPMailer\PHPMailer\PHPMailer;

require_once 'PHPMailer/PHPMailer.php';
require_once 'PHPMailer/SMTP.php';
require_once 'PHPMailer/Exception.php';

if(isset($_POST['name']) && isset($_POST['email'])){
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $body = $_POST['body'];

    $mail = new PHPMailer();

    //SMTP Settings
    $mail->isSMTP();
    $mail->Host = "smtp.gmail.com";
    $mail->SMTPAuth = true;
    $mail->Username = "ctubuddycolleague@gmail.com"; // Replace with your Gmail email address
    $mail->Password = "wbnlcfadvvqupdli"; // Replace with your Gmail password
    $mail->Port = 587; // Use TLS port 587
    $mail->SMTPSecure = "tls"; // Use TLS

    //Email Settings
    $mail->isHTML(true);
    $mail->setFrom($email, $name);
    $mail->addAddress("ctubuddycolleague@gmail.com"); // Replace with the recipient's email address
    $mail->Subject = $subject;
    $mail->Body = $body;

    $response = array();

    if($mail->send()){
        $response['status'] = "success";
        $response['message'] = "Message sent successfully!";
    }else{
        $response['status'] = "failed";
        $response['message'] = "Something is wrong: " . $mail->ErrorInfo;
    }

    echo json_encode($response);
}
?>

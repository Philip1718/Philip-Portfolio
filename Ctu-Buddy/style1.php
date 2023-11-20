<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];

    // Here, you can add code to validate the email address and store it in a database.
    // For now, let's just display a thank you message.
    echo "<div class='container'>";
    echo "<h1>Thank You!</h1>";
    echo "<p>You have successfully subscribed to our newsletter.</p>";
    echo "</div>";
}
?>

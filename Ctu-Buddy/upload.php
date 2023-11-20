<?php
$uploadDir = 'C:\xampp\htdocs\Phase2_Shadows_2023\Phase2_Shadows_2023\uploads/';  // Absolute path to store uploaded files

if (isset($_POST['resourceName']) && isset($_FILES['resourceFile'])) {
    $resourceName = $_POST['resourceName'];
    $resourceFile = $_FILES['resourceFile'];
    $resourceCategory = $_POST['resourceCategory'];
    $resourceTags = isset($_POST['resourceTags']) ? $_POST['resourceTags'] : '';

    $uploadedFile = $uploadDir . basename($resourceFile['name']);

    if (move_uploaded_file($resourceFile['tmp_name'], $uploadedFile)) {
        // File uploaded successfully.
        echo "File uploaded successfully.";
    } else {
        // Error uploading file.
        echo "Sorry, there was an error uploading your file.";
    }
} else {
    // Invalid request.
    echo "Invalid request.";
}
?>

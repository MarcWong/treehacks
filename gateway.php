<?php
header("content-Type: text/html; charset=Utf-8"); 
if ($_FILES["img"]["error"] > 0)
  {
  echo "no image";
  }
  else{
    $folder = 'img/';
    $filename = "output.jpg";
    move_uploaded_file($_FILES['img']['tmp_name'], $folder.$filename);
  }
?>

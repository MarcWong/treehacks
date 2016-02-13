<?php
if ($_FILES["file"]["error"] > 0)
  {
  echo "Error";
  }
else
  {
  $filename = "output.png";
  move_uploaded_file($_FILES['file']['tmp_name'],$filename);
  }
?>

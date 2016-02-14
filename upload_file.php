<?php
if ($_FILES["file"]["error"] > 0)
  {
  echo "Error";
  }
else
  {
  $filename = "output.jpg";
  move_uploaded_file($_FILES['file']['tmp_name'],$filename);
  chmod($filename, 0777);
echo "haha";
$a = exec("opencv.exe");
if($a==0)echo "opencv.exe successfully executed";
else "opencv.exe haven't been executed";
  }
?>

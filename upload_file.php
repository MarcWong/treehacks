<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="treehacks 2016">
    <meta name="author" content="">
    
    <title>treehacks 2016</title>
    
    <!-- Bootstrap -->
    <link href="lib/css/bootstrap.min.css" rel="stylesheet">
    <link rel="icon" type="image/png" href="resources/img/favicon.png">
    
    <link href="common.css" rel="stylesheet">

</head>
<body>
<?php
if ($_FILES["file"]["error"] > 0)
  {
  echo "Error";
  }
else
  {
  $filename = "input.jpg";
  move_uploaded_file($_FILES['file']['tmp_name'],$filename);
  chmod($filename, 0777);
//echo "haha";
$a = exec("opencv.exe");
//if($a==0)echo "opencv.exe successfully executed";
//else "opencv.exe haven't been executed";
  }
?>
<div class="row">
<div class="col-lg-6 col-lg-offset-3">
<img src="output.jpg"></img>
</div>
</div>
<div class="row">
<div class="col-lg-6 col-lg-offset-3">
<a href="new_pc/index.html"><button class="btn btn-default btn-lg">back to homepage</button></a>
</div>
</div>
</body>

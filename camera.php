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
$a = exec("/home/pi/webcam/webcam.sh");
//if($a==0)echo "opencv.exe successfully executed";
//else "opencv.exe haven't been executed";
?>
<div class="row">
<div class="col-lg-6 col-lg-offset-3">
<img src="inputcamera.jpg"></img>
</div>
</div>
<div class="row">
<div class="col-lg-6 col-lg-offset-3">
<a href="new_pc/index.html"><button class="btn btn-default btn-lg">back to homepage</button></a>
</div>
</div>
</body>

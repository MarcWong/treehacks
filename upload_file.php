<?php
if ($_FILES["file"]["error"] > 0)
  {
   echo "Error";
  }
else
  {
   $dir = "resources/PictureMagic/";
   //$filename = date("hisa") . ".jpg";
   $filename="input.jpg";
   $path = $dir.$filename;
   $light=htmlspecialchars(@$_POST['light']);
   //echo $filename;
   move_uploaded_file($_FILES['file']['tmp_name'],$path);
   chmod($path, 0777);
   //echo "haha";
   //$a = exec("python resources/PictureMagic/main.py",$dir.$filename,$light);
   $a = exec("python resources/PictureMagic/main.py");
   if($a==0)echo "main.py successfully executed";
   else "main.py haven't been executed";
   //$b=exec("opencv.exe");
   while(1){
   //if (file_exists("file.txt"))
     if (file_exists("output.png"))
     break;
   };
   
   echo "<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='utf8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <meta name='description' content='treehacks 2016'>
    <meta name='author' content=''>
    <title>treehacks 2016</title>
    <!-- Bootstrap -->
    <link href='lib/css/bootstrap.min.css' rel='stylesheet'>
    <link rel='icon' type='image/png' href='resources/img/favicon.png'>
    <link href='common.css' rel='stylesheet'>
</head>
<body>
<div class='row'>
<div class='col-lg-6 col-lg-offset-3'>
<img src='$filename'></img>
</div>
</div>
<div class='row'>
<div class='col-lg-6 col-lg-offset-3'>
<a href='new_pc/index.html'><button class='btn btn-default btn-lg'>back to homepage</button></a>
</div>
</div>
</body>";
  }

?>

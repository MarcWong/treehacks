<?php
  if(!@$FILES['img']){
    report(1,"no image");
  }
  else{
    $folder='img/';
    $filename = "output.png";
    move_uploaded_file($_FILES["img"]["tmp_name"], $folder.$filename);
  }
>

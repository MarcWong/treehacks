<?php
require("api.php");

$action=$_GET['action'];

if($action=="add"){
	
	$name=htmlspecialchars(@$_POST['name']);
	$school=htmlspecialchars(@$_POST['school']);
	$gender=htmlspecialchars(@$_POST['gender']);
	$email=htmlspecialchars(@$_POST['email']);
	$phone=htmlspecialchars(@$_POST['phone']);
	$ifgroup=htmlspecialchars(@$_POST['ifgroup']);
	
	$phone = preg_replace("[-]", "", $phone);
	
  $name=addslashes(trim($name));
	$gender=addslashes(trim($gender));
	$school=addslashes(trim($school));
	$email=addslashes(trim($email));
	$phone=addslashes(trim($phone));

  if (strlen($name)==0) {
    report(1, "Please enter a name!");
  } else if ($gender!="male"&&$gender!="female") { 
  	report(2,"Please select a valid gender!");
  } else if (strlen($school)==0) {
    report(3, "Please enter your school!");
  } else if (!preg_match ("/^[a-z0-9A-Z_.]+@[a-z0-9A-Z._\-]+\.[a-zA-Z]+$/", $email)) {
  	report(4,"Please enter a valid email!"); 
  } else if (!preg_match ("/^[0-9]+$/", $phone) || strlen($phone) != 11){
  	report(5,"Please enter a valid Chinese cellphone number!");
  } else {
    $code=add($name, $gender, $school, $ifgroup, $email, $phone);
    if ($code==0){ 
      report(0,"Register successful. Thank you!");
    } else {
      report(-1, "Internal server error. Please contact the administrator.");
    }
	}

}

$mysqli->close();
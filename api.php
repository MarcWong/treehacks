<?php


	$mysqli = new mysqli("localhost","root","iloveeecs","hackpku");
	date_default_timezone_set("Asia/Shanghai");
    
if (mysqli_connect_errno( )) {
  die('Could not connect: ' . mysql_error());
} else {
  $mysqli->set_charset("gbk");
}



function get_client_ip() {
	return getenv('HTTP_CLIENT_IP')?:
  getenv('HTTP_X_FORWARDED_FOR')?:
  getenv('HTTP_X_FORWARDED')?:
  getenv('HTTP_FORWARDED_FOR')?:
  getenv('HTTP_FORWARDED')?:
  getenv('REMOTE_ADDR');
}

function add($name, $gender, $school, $ifgroup, $email, $phone){
  global $mysqli;
  
  $name=addslashes(trim($name));
	$gender=addslashes(trim($gender));
	$school=addslashes(trim($school));
	$email=addslashes(trim($email));
	$phone=addslashes(trim($phone));
	$ip=addslashes(trim(get_client_ip()));
	$time=time();

	$stmt=$mysqli->prepare("insert into register (name, gender, school, ifgroup, email, phone, ip, ts) values (?,?,?,?,?,?,?,?)");
	$stmt->bind_param("ssssssss", $name, $gender, $school, $ifgroup, $email, $phone, $ip, $time);
  $val=$stmt->execute()?0:-1;
  $stmt->close();
  return $val;
}


function report($code,$msg){
	echo(json_encode(
		array(
		"code"=>$code,
		"msg"=>$msg
		)));
}

	
?>

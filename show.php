<!--
#show.php
#insert the form to the database
# 1300012848 10/11/2015 11:16
#############################################
-->
<HTML>
<HEAD><TITLE>Result Page</TITLE>
<meta http-equiv="Content-type" content="text/html;" charset="UTF-8" />
<link rel="stylesheet" type="text/css" href="css/mycss.css" />
</HEAD>
<H3>Result Page</H3>
<BODY>
<?php
#db connect
@$con = mysql_connect("qdm21120568.my3w.com","qdm21120568","iloveeecs");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }
#db select
mysql_select_db("qdm21120568_db", $con);

#delete
@$id=$_REQUEST["choose"];
echo "last deleted Guest_ID= ";
echo $id;
echo "<br>";
mysql_query("DELETE FROM Guest_Table WHERE Guest_ID='$id' ");

#table select
$result = mysql_query("SELECT * FROM Guest_Table");
echo "<form action = 'show.php' method = 'POST'>";
echo"<table border='border'>";
echo"<th>ID<td>Guest Name</td><td>Age</td><td>Gender</td><td>E-mail</td><td>choose</td></th>";
while($row = mysql_fetch_array($result))
{
  echo "<tr><td>";
  echo $row["Guest_ID"];
  echo  "</td><td>" ;
  echo $row['Guest_Name'];
  echo "</td><td>";
  echo $row['Age'];
  echo "</td><td>";
  echo $row['Gender'];
  echo "</td><td>";
  echo $row['E_mail'];
  echo "</td><td>";
  echo $a = $row["Guest_ID"];
  echo "<input type = 'radio' name='choose' value='$a'>";
  echo "</td></tr>" ;
 }
echo"</table>";
echo "<input type='submit' value='delete'/></form>";
?>
<div><a href="index.html" id = "return"><img src="img/logo0.png" /></a></div>
</BODY>
</HTML>

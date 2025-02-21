<?php

$fname=$_REQUEST['firstname'];
include_once('db.php');



$sql="select * from attendance where name='$fname' and adate=CURRENT_DATE()";
$res=execute( $sql );

$row=$res->fetch_object();

if( !isset($row)){
			
$sql="insert into attendance(name,adate) values('$fname',CURRENT_DATE())";

$res=execute( $sql );


}
			
?>
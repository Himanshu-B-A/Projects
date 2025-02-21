<?php


	include_once('homepagenav.php');
	include_once('db.php');
	
	$sino=$_REQUEST['sino'];
	
	$sql="delete from attendance where id=$sino";
	
	$res=execute( $sql );
	
	echo "<center><font color=blue size=10>Record is deleted</font>
	</center>";
	
	
	
	echo "<br/><center><a href=viewdocs.php>Return</a></center>";
	
?>
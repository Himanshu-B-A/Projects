<?php

	include_once('homepagenav.php');
	include_once('db.php');
	
	$sql="select * from attendance ";
	
	
	
	$res=execute( $sql );
	
	echo "<table align=center class='table table-hover table-striped' >";
	echo "<tr><th>Name</th><th>Date</th><th>&nbsp;</th></tr>";
	
	while( $row=$res->fetch_object() )
	{
	
	echo "<tr><td>$row->name</td><td>$row->adate </td>";
	
	
	
	?>
	
	<td>
	<a href="deletedocs.php?sino=<?php echo $row->id ?>"  class="btn btn-danger" onclick="return confirm('Are You Sure ??');" >Delete</a>
	</td>
	<?php
	}
	
	echo "</table>";
    ?>
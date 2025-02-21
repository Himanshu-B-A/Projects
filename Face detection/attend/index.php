<!DOCTYPE html>


<html>

<head>



<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/bootstrap.min.css" />

<script src="jquery-2.2.0.js" >
</script>


<script src="js/bootstrap.min.js" >
</script>


<script>

$( document ).ready( function(){

	//alert("hii");

	$("#result").hide();
	
	
	
	
	
	$("#logintype").change( function(){
	
	
		$("#uname").val("");
		$("#pwd").val("");
		
	
	
	});
	
	
	
	$("#f1").submit( function(){
	
		
		if( $("#logintype").val()=="admin"  )
		{
			if( $("#uname").val()=="admin" && $("#pwd").val()=="admin" )
			{
				location.href="homepage.php";
			}
			else
			{
				$("#result").css("background-color","red").html("<center><font color=white size=3>Invalid user name / Password</font></center>").fadeIn(2000).fadeOut(5000);
			}
			
		}
		else if( $("#logintype").val()=="student"  ||  $("#logintype").val()=="employer"   )
		{			

					alert("verifying..");
			
					$.get(
									"chklogin.php",
									{
										uname:$("#uname").val(),pwd:$("#pwd").val(),logintype:$("#logintype").val()
									},
									
									function( data )
									{
									
										alert(data);
										
										if( data==1 )
										{
										location.href="studenthomepage.php";
										}
										else if( data==2 )
										{
										location.href="employerhomepage.php";
										}
										else if( data==0 )
										{
										$("#result").css("background-color","red").html("<center><font color=white size=3>Invalid user name / Password</font></center>").fadeIn(2000).fadeOut(5000);
										}
										else if( data==-1 )
										{
										$("#result").css("background-color","red").html("<center><font color=white size=3>Account not yet Approved</font></center>").fadeIn(2000).fadeOut(5000);
										}

									}
					
					        );
		}
		else 
		{
		
		
		}
	
	return(false);
	});

});

</script>


<style>


table{
/* margin-top:100px;
border-radius:20px; */
width:auto;
/* background:-webkit-linear-gradient(top,purple,ivory); */
}
td{
text-align:center;
}
input[type='text'],input[type='password'],select{

width:250px;
height:40px;
border-radius:10px;
padding-left:10px;
outline:none;
color:blue;
text-color:blue;
font-weight:bold;
}

body{

	/* //background-color:#333333; */
	background-image:url(img/bihe.jpg);
	background-size:cover;
}

h1{
/* color:white; */
}
</style>

</head>

<body>

<div class="container-fluid bg-primary text-white text-center m-5" >

<H1>Face recognition based attendance monitoring system</H1>
</div>

<center>
	<img src="img/login.jpg" alt="" class="img img-responsive">
</center>
<div class="container bg-info m-5" style="background-color:slateblue; color:white; margin-top:10px;"  >

<h1>Login Form</h1>

	<form name="f1" id="f1" >
	

	<table class="table"  >
	
	<tr>
	<td style="border-top:0px;" >
	
	<select name="logintype" id="logintype" >
	
	<option value="#" > ---- Login type ---- </option>
	<option value="admin" >Admin </option>
	<!-- <option value="student" >Student</option>
	<option value="employer" >Employer</option> -->
	
	
	</select>
	</td>
	</tr>
		
	
	<tr>
	<td style="" >
	<input type="text" name="uname" id="uname" placeholder="User Name" required=required  />
	</td>
	</tr>
	
	<tr>
	<td>
	<input type="password" name="pwd" id="pwd" placeholder="Password" required=required />
	</td>
	</tr>
	
	
	<tr>
	<td>
	<input type="submit"  value=" Login " class="btn btn-danger btn-lg btn-block"  />
	</td>
	</tr>
	
	</table>
	
	</form>

</div>


<br/>



<div class="well" id="result" >
</div>

</body>
</html>
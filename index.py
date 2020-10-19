# coding: utf-8

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<script type="text/javascript" src="static/javascript.js"></script>
		<title>test foto</title>
				<script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
		

	</head>
	<body>
		<div id="contener">	
			<p>nom </p>
			<input id="name"></input>
			<br>
			<p>prenom</p>
			<input id="prenom"></input>
			<br>
			<p>mail</p>
			<input id="mail" onblur="blocage_mail()"></input>
			<br>
			<p>proffesion</p>
			<input id="profession"></input>
			<br>
			<p>date</p>
			<input type="date" id="date" name="trip-start"
       		value="2020-10-19"
       		min="2020-01-01" max="2020-12-31">

			<br>
			<button id="button" onclick="envoyer()">envoyer</button>

			
		</div>
	</body>
</html>
"""

print(html)


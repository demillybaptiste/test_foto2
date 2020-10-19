function envoyer(){
	
	var nom=document.getElementById("name").value;

	var prenom=document.getElementById("prenom").value;

	var mail=document.getElementById("mail").value;

	var profesion=document.getElementById("profession").value;

	var calendrier=document.getElementById("date").value;
    $.ajax({
       type : 'POST',
       data : '{"nom":"' + nom+'","prenom":"'+prenom+'","mail":"'+mail+'","profesion:"'+profesion+'","date":"'+calendrier+ '"}'
    });
   


}


function blocage_mail(){
	var mail=document.getElementById("mail").value;
	if(mail ==null || mail==""){
		document.getElementById("button").disabled = true;
	}
	else{
		document.getElementById("button").disabled = false;
	}


}
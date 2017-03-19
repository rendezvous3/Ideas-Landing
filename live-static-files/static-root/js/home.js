$(document).ready(function(){
	$(".join-form").submit(function(e){
		e.preventDefault();
		console.log($(this).serialize())
		var joinEmailAPIEndpoint = "/api/email/join/";
		//var joinEmailAPIEndpoint = "{% url 'api-email-join' %}";
		$.ajax({
			method: "POST",
			data:   $(this).serialize(),
			url: joinEmailAPIEndpoint,
			success: function(data){
				console.log(data)
				//$(this).fadeOut();
			},
			error: function(data){
				console.log("error")
				console.log(data)
			}
		})
	});
});
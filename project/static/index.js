window.onload = () => {
	$('#sendbutton').click(() => {
		imagebox = $('#imagebox1')
		input = $('#imageinput')[0]
		if(input.files && input.files[0])
		{
			let formData = new FormData();
			formData.append('image' , input.files[0]);
			$.ajax({
				url: "http://localhost:5000/detectObject", // fix this to your liking
				type:"POST",
				data: formData,
				cache: false,
				processData:false,
				contentType:false,
				error: function(data){
					console.log("upload error" , data);
					console.log(data.getAllResponseHeaders());
				},
				success: function(data){
					console.log(data);
					bytestring = data['status']
					image = bytestring.split('\'')[1]
					imagebox.attr('src' , 'data:image/jpeg;base64,'+image);
					imagebox.height(400);
					imagebox.width(600);
				}
			});
		}
	});
};



function readUrl(input){
	$('#imagebox1').height(0)
	$('#imagebox1').width(0)
	imagebox = $('#imagebox')
	console.log("evoked readUrl")
	if(input.files && input.files[0]){
		let reader = new FileReader();
		reader.onload = function(e){
			// console.log(e)
			
			imagebox.attr('src',e.target.result); 
			imagebox.height(400);
			imagebox.width(600);
		}
		reader.readAsDataURL(input.files[0]);
	}

	
}
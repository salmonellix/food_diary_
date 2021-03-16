function deleteItem(items){

			console.log('Delete clicked')
            var url = '{% url product-delete 1 2 %}';
			url = url.replace(1, items[0]);
			url = url.replace(2, items[1]);

			fetch(url, {
				method:'DELETE',
				headers:{
					'Content-type':'application/json',
					'X-CSRFToken':csrftoken,
				}
			})
		}


var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function(e){
	e.preventDefault()
	console.log('Form submitted')
	var url = '{% url product-create %}';

	var product_name = document.getElementById('product-name').value
	var proteins = document.getElementById('proteins').value
	var carbs = document.getElementById('carbs').value
	var fats = document.getElementById('fats').value
	var calories_100 = document.getElementById('calories/100g').value
	var amount = document.getElementById('amount').value

	fetch(url, {
		method:'POST',
		headers:{
			'Content-type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'product_name':product_name, 'proteins': proteins, 'carbs': carbs, 'fats': fats, 'calories_100': calories_100, 'amount': amount })
	}

	)
})


function addItem(){
	var form = document.getElementById('form-wrapper')
	var url = '{% url product-create %}';
	var product_name = document.getElementById('product-name').value
	var proteins = document.getElementById('proteins').value
	var carbs = document.getElementById('carbs').value
	var fats = document.getElementById('fats').value
	var calories_100 = document.getElementById('calories/100g').value
	var amount = document.getElementById('amount').value

		fetch(url, {
		method:'POST',
		headers:{
			'Content-type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'product_name':product_name, 'proteins': proteins, 'carbs': carbs, 'fats': fats, 'calories_100': calories_100, 'amount': amount })
	})



}
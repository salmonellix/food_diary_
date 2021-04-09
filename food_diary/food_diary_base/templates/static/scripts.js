
function getCookie(name) {
		    var cookieValue = null;
		    if (document.cookie && document.cookie !== '') {
		        var cookies = document.cookie.split(';');
		        for (var i = 0; i < cookies.length; i++) {
		            var cookie = cookies[i].trim();
		            // Does this cookie string begin with the name we want?
		            if (cookie.substring(0, name.length + 1) === (name + '=')) {
		                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                break;
		            }
		        }
		    }
		    return cookieValue;
		}
		var csrftoken = getCookie('csrftoken');

		var activeItem = null
		var list_snapshot = []


function buildList(){
			var wrapper = document.getElementById('list-wrapper');
			//wrapper.innerHTML = ''
			var url = 'http://127.0.0.1:8000/exam/';

			fetch(url)
			.then((resp) => resp.json())
			.then(function(data){
				console.log('Data:', data);

				var list = data;
				for (var i in list){
					var item = `
                    <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                            <div style="flex:7">
                            <span class="title"> Title: ${list[i].title}</span>
                            <span id ="description" " class="description"> Description: ${list[i].description}</span>
                            <span class="location"> Location: ${list[i].location}</span>
                            <span class="id_e"> ID: ${list[i].id_exam}</span>


                            </div>
                            <div style="flex:1">
                                <button class="btn edit">EDIT </button>
                            </div>
                             <div style="flex:1">
                                <button class="btn delete" onclick="deleteItem(${list[i].id_exam})" >DELETE</button>
                            </div>
                             <div style="flex:1">
                                <button class="btn delete" onclick="window.location.href='http://127.0.0.1:8000/front/examslist/grades/${list[i].id_exam}/'">GRADES</button>
                            </div>
                            </div>
						`
					wrapper.innerHTML += item
								}
				for (var i in list){
					var editBtn = document.getElementsByClassName('edit')[i]
					var deleteBtn = document.getElementsByClassName('delete')[i]
					var title = document.getElementsByClassName('title')[i]


					editBtn.addEventListener('click', (function(item){
						return function(){
							editItem(item)
						}
					})(list[i]))


					deleteBtn.addEventListener('click', (function(item){
						return function(){
							deleteItem(item)
						}
					})(list[i]))


					// title.addEventListener('click', (function(item){
					// 	return function(){
					// 		strikeUnstrike(item)
					// 	}
					// })(list[i]))


				}

			})}

		function editItem(item){
			console.log('Item clicked:', item)
			activeItem = item
			document.getElementById('description').value = activeItem.description
		}


		function deleteItem(item){

			console.log('Delete clicked')
			fetch(`http://127.0.0.1:8000/front/exam-delete/${item}/`, {
				method:'DELETE',
				headers:{
					'Content-type':'application/json',
					'X-CSRFToken':csrftoken,
				}
			}).then((response) => {
				clearAll()
				buildList()
			})
		}

		var form = document.getElementById('form-wrapper')
		form.addEventListener('submit', function(e){
			e.preventDefault()
			console.log('Form submitted')
			var url = 'http://127.0.0.1:8000/front/exam-create/'
			if (activeItem != null){
				var url = `http://127.0.0.1:8000/front/exam-update/${activeItem.id_exam}/`
				console.log(url)
				activeItem = null
			}

			var title = document.getElementById('title').value
			var description = document.getElementById('description').value
			var location = document.getElementById('location').value
			// var id_s = document.getElementById('id_s').value
			var id_s = []
			var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')
			for (var i = 0; i < checkboxes.length; i++) {
			  id_s.push(parseInt(checkboxes[i].value))
			}
			// var id_s = document.querySelector('.checkbox:checked').value;
			console.log(id_s)
			fetch(url, {
				method:'POST',
				headers:{
					'Content-type':'application/json',
					'X-CSRFToken':csrftoken,
				},
				body:JSON.stringify({'title':title, 'description': description, 'location': location, 'student_id': id_s})
			}

			).then(function(response){
				clearAll()
				buildList()
				document.getElementById('form').reset()
			})
		})






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


function searchDay() {
var wrapper = document.getElementById('list-wrapper-search');
			//wrapper.innerHTML = ''
			var searchTXT = document.getElementById("search").value;
			var url = 'http://127.0.0.1:8000/exam/?search=' + searchTXT;

			fetch(url)
			.then((resp) => resp.json())
			.then(function(data){
				console.log('Data:', data);

				var list = data;
				for (var i in list){
					var item = `
                    <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                            <div style="flex:7">
                            <span class=title"> Title: ${list[i].title}</span>
                            <span class=title"> Description: ${list[i].description}</span>
                            <span class=title"> Location: ${list[i].location}</span>
                            <span class=title"> ID: ${list[i].id_exam}</span>


                            </div>
                            <div style="flex:1">
                                <button class="btn edit">EDIT </button>
                            </div>
                             <div style="flex:1">
                                <button class="btn delete" onclick="deleteItem(${list[i].id_exam})" >DELETE</button>
                            </div>
                             <div style="flex:1">
                                <button class="btn delete" onclick="window.location.href='http://127.0.0.1:8000/front/examslist/grades/${list[i].id_exam}/'">GRADES</button>
                            </div>
                            </div>
                            </div>
						`
					wrapper.innerHTML += item
								}})}
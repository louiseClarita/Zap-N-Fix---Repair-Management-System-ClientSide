
const ratings = document.querySelectorAll('.rating')
const ratingsContainer = document.querySelector('.ratings-container')
const sendBtn = document.querySelector('#send')
const panel = document.querySelector('#panel')
let selectedRating = 'Satisfied'

ratingsContainer.addEventListener('click', (e) => {
    if(e.target.parentNode.classList.contains('rating')) {
        removeActive()
        e.target.parentNode.classList.add('active')
        selectedRating = e.target.nextElementSibling.innerHTML
    }
    if(e.target.classList.contains('rating')) {
        removeActive()
        e.target.classList.add('active')
        selectedRating = e.target.nextElementSibling.innerHTML
    }

})
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

sendBtn.addEventListener('click', (e) => {


 if (selectedRating) {

        var panelContainer = document.getElementById('panel');
        var id = panelContainer.dataset.recordId;
        var rating = 1.1
        var divValue = document.getElementById('note');


       var csrfToken = window.csrfToken;
       //  var csrfToken = getCookie('csrftoken');  // Get the value of the CSRF token from the cookie

            if(selectedRating == "Neutral")
            {
            rating = 3.1
            }else if(selectedRating == "Unhappy"){
             rating = 0.1
            }else if(selectedRating == "Satisfied"){
            rating = 5.1
            }
            if(divValue.value == divValue.placeholder){
            divValue="Didn't add a note";
            }
            var data = {
              rate: rating,
              notes: divValue.value
            };

        console.log(JSON.stringify(data))

        fetch( '/Repair/Feedback/'+id,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken' : csrfToken
        },
        body : JSON.stringify(data)

         }).then(response => {
    if (response.ok) {
      console.log('POST request was successful.');

    panel.innerHTML = `
      <br>
        Thank You!
         <br>
        Feedback : ${selectedRating}
        <br><br>We'll use your feedback to improve our customer support`
    } else {
      console.log('POST request failed. Error:', response.status);
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });




                     }else{
                       console.log("please select a rating!")
                          }
})

function removeActive() {
    for(let i = 0; i < ratings.length; i++) {
        ratings[i].classList.remove('active')
    }
}


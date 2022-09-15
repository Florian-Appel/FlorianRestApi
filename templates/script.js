async function init() {
    let url = 'https://florianappel.pythonanywhere.com/todos/';
    // console.log('1:', url);

    let response = await fetch(url);
    // console.log('2:', response);

    let json = await response.json();
    // console.log('3:', json);

    for (let i = 0; i < json.length; i++) {

        document.getElementById('show').innerHTML += `
        <div class="todos">
                <p><b>ID:</b> ${json[i].id}</p>
                <p><b>Title:</b> ${json[i].title}</p>
                <p><b>Description:</b> ${json[i].description}</p>
                <p><b>Date:</b> ${json[i].chreated_at}</p>
                <p><b>User:</b> ${json[i].user['username']}</p>
                <p><b>Online since:</b> ${json[i].time_passed} Days</p>
                <button class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--primary">
                    <i class="material-icons">delete</i>
                </button>
            </div>
            <div class="line"></div>
        `;
    }
}

function openForm() {
    document.getElementById("popupForm").style.display = "block";
    document.getElementById('backround').classList.add('backround');
}
function closeForm() {
    document.getElementById("popupForm").style.display = "none";
    document.getElementById('backround').classList.remove('backround');
}

// Test

async function sendMessage() {
    let fd = new FormData();
    let token = '{{ csrf_token }}';
    fd.append('textmessage', title.value);
    fd.append('csrfmiddlewaretoken', token);
    
    try {
        showValue.innerHTML += `
            <div id="deleteMessage" class="message-bubble">
                <span style="color: lightgray" id="test">{{request.user}}: <i style="color: darkgray">${title.value}</i>
            </div>
        `;

        // let response = await fetch('/chat/', {
        //     method: 'POST',
        //     body: fd
        // });
        // let json = await response.json();
        // console.log(json);

        document.getElementById('deleteMessage').remove();
        

        showValue.innerHTML += `
            <div class="box">
                <div class="message-bubble">
                    <span style="color: lightgray">{{request.user}}: <i>${title.value}</i> 
                </div>
            </div>
        `;
        title.value = '';

    } catch (e) {
        console.log('ERROR!', e)
    }
}
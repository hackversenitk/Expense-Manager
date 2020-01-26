setTimeout(function submitBillNameUsers() {
    var queryString = $('#add-users-section-form').serialize();
    // alert(queryString);
}, 500);

function generate() {
    var a = parseInt(document.getElementById("getNumberOfUsers").value);
    var ch = document.getElementById("ch");
    for (i = 0; i < a; i++) {
        var input = document.createElement("input");
        var btn = document.createElement("button");
        var userDiv = document.createElement("div");
        userDiv.id = "user" + i;
        userDiv.innerHTML += "user"+i;
        userDiv.appendChild(input);
        btn.innerHTML = "add";
        btn.id = 'btn' + i;
        btn.className = 'addition';
        userDiv.append(btn);
        ch.appendChild(userDiv);

        ch.innerHTML += "<br>";
    }
    var allButtons = document.querySelectorAll('.addition');

    for (let j = 0; j < allButtons.length; j++) {
        let button = allButtons[j];
        let test = "user" + j;
        button.addEventListener('click', function() {
            event.preventDefault();
            var inpt = document.createElement("input");
            inpt.id = "item-name" + j;
            var inpt2 = document.createElement("input");
            inpt2.id = "item-price" + j;
            document.getElementById(test).appendChild(inpt);
            document.getElementById(test).appendChild(inpt2);
        });
    }
}

function increment() {
    document.getElementById("getNumberOfUsers").value = parseInt(document.getElementById("getNumberOfUsers").value) + 1;
}

function decrement() {
    if(parseInt(document.getElementById("getNumberOfUsers").value) > 2) {
        document.getElementById("getNumberOfUsers").value = parseInt(document.getElementById("getNumberOfUsers").value) - 1;
    }
}

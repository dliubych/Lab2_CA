/**
 * Created by Maxim on 26.04.2015.
 */

function update() {
    setInterval(function () {
        updateLocal();
    }, 500)
}

function updateLocal() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/serverData", false);
    xmlhttp.send();

    var whatWeGot = JSON.parse(xmlhttp.responseText);
    var number = whatWeGot['number_of_clients'];
    var percents = whatWeGot['percents'];
    var results = whatWeGot['results'];
    var time = whatWeGot['time'];

    document.getElementById('clients').innerHTML = 'Clients:  ' + number;
    document.getElementById('percents').innerHTML = 'Percents: ' + percents;
    if (results != '-1') {
        document.getElementById('results').innerHTML = 'Results: ' + results;
        document.getElementById('time').innerHTML = 'Time: ' + time;
    }
}
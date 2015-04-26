/**
 * Created by Maxim on 22.04.2015.
 */
//importScripts("jquery-2.1.3.js");

function isPalindrome(str) {
    return str == str.split('').reverse().join('');
}


function getPalindromes(text, n) {
    var palindromes = [];
    for (var i = 0; i < text.length - n; i++)
        if (isPalindrome(text.substr(i, n)))
            palindromes.push(text.substr(i, n));
    return palindromes;
}

//postMessage('worker works before');

//$.ajax({
//    url: "http://localhost:8080/workerData",
//    //context: document.body,
//
//    success: function () {
//        //alert(123);
//        postMessage(data);
//        //$(this).addClass("done");
//    }
//});


//$.post("/workerData", function (data) {
//        alert("Data: " + data);
//});

xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        postMessage(xmlhttp.responseText);
};
//xmlhttp.open("GET", "/workerData", false);
//xmlhttp.send();

xmlhttp1 = new XMLHttpRequest();
xmlhttp1.open("POST", "/workerData", true);
xmlhttp1.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp1.send("data=Henry");

//$.get('http://localhost:8080/workerData', function(data) {
//    postMessage(data);
//});

//postMessage('worker works after');

//var palindromes = getPalindromes("aaa, bbb, ccc cab", 4);
//postMessage(palindromes.valueOf());

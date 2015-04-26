/**
 * Created by Maxim on 22.04.2015.
 */

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


var text, n = 100, workerNumber;
//var xmlhttpGET, xmlhttpPOST;

while (n != -1) {
    var xmlhttpGET = new XMLHttpRequest();
//xmlhttpGET.onreadystatechange = function () {
//    if (xmlhttpGET.readyState == 4 && xmlhttpGET.status == 200) {
//        var whatWeGot = JSON.parse(xmlhttpGET.responseText);
//        text = whatWeGot['text'];
//        n = whatWeGot['n'];
//        workerNumber = whatWeGot['worker_number'];
//
//        var palindromes = getPalindromes(text, n);
//
//        xmlhttpPOST = new XMLHttpRequest();
//        xmlhttpPOST.open("POST", "/workerData", true);
//        xmlhttpPOST.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//        xmlhttpPOST.send("worker_number=" + workerNumber + "&palindromes=" + palindromes);
//    }
//};
    xmlhttpGET.open("GET", "/workerData", false);
    xmlhttpGET.send();

    var whatWeGot = JSON.parse(xmlhttpGET.responseText);
    text = whatWeGot['text'];
    n = whatWeGot['n'];
    workerNumber = whatWeGot['worker_number'];

    if (n != -1) {
        var palindromes = getPalindromes(text, n);

        var xmlhttpPOST = new XMLHttpRequest();
        xmlhttpPOST.open("POST", "/workerData", true);
        xmlhttpPOST.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttpPOST.send("worker_number=" + workerNumber + "&palindromes=" + palindromes);

        //setTimeout(function () {}, 2000);
    }
}

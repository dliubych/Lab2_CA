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

while (n != -1) {
    var requestGET = new XMLHttpRequest();
    requestGET.open("GET", "/workerData", false);
    requestGET.send();

    var whatWeGot = JSON.parse(requestGET.responseText);
    text = whatWeGot['text'];
    n = whatWeGot['n'];
    workerNumber = whatWeGot['worker_number'];

    if (n != -1 && n != -2) {   // n == -1 - finish work; n == -2 - pause
        var palindromes = getPalindromes(text, n);

        var requestPOST = new XMLHttpRequest();
        requestPOST.open("POST", "/workerData", true);
        requestPOST.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        requestPOST.send("worker_number=" + workerNumber + "&palindromes=" + palindromes);
    }
}

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

//alert('lalala');
postMessage('worker works before1');

$.ajax({
    url: "http://localhost:8080/workerData",
    //context: document.body,
    success: function () {
        //alert(123);
        postMessage(data);
        //$(this).addClass("done");
    }
});

//$.get('/workerData', function(data) {
//    postMessage(data);
//});

postMessage('worker works after');

//var palindromes = getPalindromes("aaa, bbb, ccc cab", 4);
//postMessage(palindromes.valueOf());

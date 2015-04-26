/**
 * Created by Maxim on 22.04.2015.
 */

function f() {
    //alert('1');

    var worker = new Worker("scripts/worker.js");

    worker.onmessage = function (event) {
        alert(event.data);
    };



}

/**
 * Created by Maxim on 22.04.2015.
 */

function f() {
    var worker = new Worker("scripts/worker.js");

    worker.onmessage = function (event) {
        alert(event.data);
    };
}

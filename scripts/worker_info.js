/**
 * Created by Maxim on 22.04.2015.
 */

function startWorker() {
    var worker = new Worker("scripts/worker.js");

    worker.onmessage = function (event) {
        document.getElementById('info').innerHTML = event.data;
        //alert(event.data);
    };
}

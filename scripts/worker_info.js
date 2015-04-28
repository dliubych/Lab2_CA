/**
 * Created by Maxim on 22.04.2015.
 */

function startWorker() {
    var worker = new Worker("scripts/worker.js");

    worker.onmessage = function (event) {
        //var data = JSON.parse(event.data);
        //        //alert(data);
        //
        //var state = data['state'];
        //var palindromes = data['palindromes'];
        //
        //if (state == 'work')
        //    document.getElementById('state').innerHTML = 'Finding palindromes in text';
        //else if (state == 'pause')
        //    document.getElementById('state').innerHTML = 'Paused';
        //else if (state == 'stop')
        //    document.getElementById('state').innerHTML = 'Finished';
        //
        //if (state == 'wait')
        //    document.getElementById('state').innerHTML = 'Waiting for first data';
        //else
        //    document.getElementById('info').innerHTML = 'Last founded palindromes are: ' + palindromes;

        document.getElementById('info').innerHTML = event.data;
    };
}

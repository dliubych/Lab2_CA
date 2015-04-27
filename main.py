from bottle import *
import bottle


start_time = time.time()
sent_parts = []
free_parts = []
sent_parts_without_deleting = []
received_parts = []
all_palindromes = []
n = 5
finished = []


# Returns static file. Used for getting JavaScript files from /scripts folser
@bottle.get('/scripts/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./scripts/')


# Returns worker page
@bottle.get('/')
def worker():
    return static_file('worker.html', root='./')


# Returns server page
@bottle.get('/server')
def server():
    return static_file('server.html', root='./')


# Returns data for server: number of clients, percents
# of done work and if work finished results with working time
@get('/serverData')
def worker_get():
    number_of_clients = len(sent_parts) - len(received_parts)
    percents = len(received_parts)
    if finished == [] and 100 <= percents:
        finished.append(1)

        working_time = time.time() - start_time
        if 100 in received_parts:
            received_parts.remove(100)
            if 100 not in received_parts:
                received_parts.append(100)
        return {'number_of_clients': number_of_clients,
                'percents': percents, 'results': all_palindromes,
                'time': working_time}
    else:
        return {'number_of_clients': number_of_clients,
                'percents': percents, 'results': '-1', 'time': 'none'}


# Returns data for worker: his id and text
@get('/workerData')
def worker_get():
    for i in range(1, 101):
        if i not in sent_parts and i not in received_parts:
            sent_parts.append(i)
            worker_text = text[(len(text) - n) *
                               (i - 1) / 100: (len(text) - n) * i / 100 + n]
            return {'n': n, 'text': worker_text, 'worker_number': i}

    for i in range(1, 101):
        if i not in received_parts:
            worker_text = text[(len(text) - n) *
                               (i - 1) / 100: (len(text) - n) * i / 100 + n]
            return {'n': n, 'text': worker_text, 'worker_number': i}

    # Message that worker needs to stop
    return {'n': -1, 'text': '', 'worker_number': -1}


# Processes data we got from worker: his id and founded palindromes
@post('/workerData')
def worker_post():
    worker_number = request.forms.get('worker_number')
    palindromes = request.forms.get('palindromes')

    if worker_number not in received_parts:
        received_parts.append(int(worker_number))

    # For debugging
    print('Part #%s finished' % worker_number)
    for i in palindromes.split(','):
        if i != '' and '\n' not in i and i not in all_palindromes:
            all_palindromes.append(i)


file_with_text = open('text.txt', 'r')
text = file_with_text.read()
run(host='0.0.0.0', port=8080, debug=True)

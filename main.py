from bottle import *
import bottle


sent_parts = []
free_parts = []
sent_parts_without_deleting = []
received_parts = []
all_palindromes = []
n = 100
finished = []
start_time = 0
finish_time = 0
number_of_parts_for_workers = 100
file_with_text = open('text.txt', 'r')
text = file_with_text.read()
pause_server = False


# Returns static file. Used for getting JavaScript files from /scripts folder
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
    if number_of_parts_for_workers == percents:
        return {'number_of_clients': number_of_clients,
                'percents': percents, 'results': all_palindromes,
                'time': finish_time - start_time}
    else:
        return {'number_of_clients': number_of_clients,
                'percents': percents, 'results': '-1',
                'time': finish_time - start_time}


# Processes data we got from worker: his id and founded palindromes
@post('/serverData')
def server_post():
    data = request.forms.get('data')
    global pause_server, sent_parts, received_parts
    if data == 'pause':
        pause_server = True
    elif data == 'resume':
        pause_server = False
    elif data == 'restart':
        pause_server = False
        sent_parts = []
        received_parts = []


# Returns data for worker: his id and text
@get('/workerData')
def worker_get():
    if pause_server:
        return {'state': 'pause', 'text': '', 'worker_number': -1}

    global start_time
    if start_time == 0:
        start_time = time.time()

    for i in range(1, number_of_parts_for_workers + 1):
        if i not in sent_parts and i not in received_parts:
            sent_parts.append(i)
            worker_text = text[(len(text) - n) * (i - 1) /
                               number_of_parts_for_workers: (len(text) - n) * i / number_of_parts_for_workers + n]
            return {'state': 'work', 'text': worker_text, 'worker_number': i}

    for i in range(1, number_of_parts_for_workers + 1):
        if i not in received_parts:
            worker_text = text[(len(text) - n) *
                               (i - 1) / number_of_parts_for_workers: (len(text) - n) * i / number_of_parts_for_workers + n]
            return {'state': 'work', 'text': worker_text, 'worker_number': i}

    # Message that worker needs to stop
    return {'state': 'stop', 'text': '', 'worker_number': 0}


# Processes data we got from worker: his id and founded palindromes
@post('/workerData')
def worker_post():
    worker_number = request.forms.get('worker_number')
    palindromes = request.forms.get('palindromes')

    if int(worker_number) not in received_parts\
            and int(worker_number) in sent_parts:
        received_parts.append(int(worker_number))

    if len(received_parts) == number_of_parts_for_workers:
        global finish_time
        finish_time = time.time()

    for i in palindromes.split(','):
        if i not in all_palindromes:
            all_palindromes.append(i)

    # For debugging
    print('Part #%s finished' % worker_number)


run(host='0.0.0.0', port=8080, debug=True)

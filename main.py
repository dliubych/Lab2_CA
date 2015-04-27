from bottle import *
import bottle
import time

start_time = time.time()
sent_parts = []
free_parts = []
sent_parts_without_deleting = []
received_parts = []
all_palindromes = []
n = 5


@bottle.get('/scripts/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./scripts/')


@bottle.get('/')
def worker():
    return static_file('worker.html', root='./')


@bottle.get('/server')
def server():
    return static_file('server.html', root='./')


@get('/serverData')
def worker_get():
    number_of_clients = len(sent_parts) - len(received_parts)
    percents = len(received_parts)
    if 100 <= percents:
        print('Time of program work is %s seconds' % (time.time() - start_time))
        return {'number_of_clients': number_of_clients, 'percents': percents, 'results': all_palindromes}
    else:
        return {'number_of_clients': number_of_clients, 'percents': percents, 'results': '-1'}


@get('/workerData')
def worker_get():
    for i in range(1, 101):
        if i not in sent_parts and i not in received_parts:
            sent_parts.append(i)
            worker_text = text[(len(text) - n) * (i - 1) / 100: (len(text) - n) * i / 100 + n]
            # print('worker #%d working on \'%s\'' % (i, worker_text))
            return {'n': n, 'text': worker_text, 'worker_number': i}

    for i in range(1, 101):
        if i not in received_parts:
            worker_text = text[(len(text) - n) * (i - 1) / 100: (len(text) - n) * i / 100 + n]
            # print('worker #%d working on \'%s\'' % (i, worker_text))
            return {'n': n, 'text': worker_text, 'worker_number': i}

    # for i in all_palindromes:
    #     print(i)
    return {'n': -1, 'text': '', 'worker_number': -1}  # Message that worker needs to stop


@post('/workerData')
def worker_post():
    worker_number = request.forms.get('worker_number')
    palindromes = request.forms.get('palindromes')

    if worker_number not in received_parts:
        received_parts.append(int(worker_number))

    # for i in received_parts:
    #     received_parts.remove(i)
    #     received_parts.append(i)
    #     # for j in received_parts:


    # Just debugging
    print('Part #%s finished' % worker_number)
    for i in palindromes.split(','):
        if i != '' and '\n' not in i and i not in all_palindromes:
            all_palindromes.append(i)


file_with_text = open('text.txt', 'r')
text = file_with_text.read()
run(host='localhost', port=8080, debug=True)

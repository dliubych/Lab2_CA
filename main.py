from bottle import *
import bottle

sent_parts = []
free_parts = []
received_parts = []
all_palindromes = []
n = 4


@bottle.get('/scripts/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./scripts/')


@bottle.get('/')
def index():
    return static_file('index.html', root='./')


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
            # sent_parts.append(i)
            worker_text = text[(len(text) - n) * (i - 1) / 100: (len(text) - n) * i / 100 + n]
            # print('worker #%d working on \'%s\'' % (i, worker_text))
            return {'n': n, 'text': worker_text, 'worker_number': i}

    for i in all_palindromes:
        print(i)
    return {'n': -1, 'text': '', 'worker_number': -1}   # Message that worker needs to stop


@post('/workerData')
def worker_post():
    worker_number = request.forms.get('worker_number')
    palindromes = request.forms.get('palindromes')

    if worker_number not in received_parts:
        received_parts.append(int(worker_number))
        if int(worker_number) in sent_parts:
            sent_parts.remove(int(worker_number))

    # Just debugging
    # print('I`m worker #%s and I found next palindromes:' % worker_number)
    print('Part #%s finished' % worker_number)
    was_something = False
    for i in palindromes.split(','):
        if '\n' not in i and i not in all_palindromes:
            all_palindromes.append(i)
            # was_something = True
            # print(i)
    # if not was_something:
    #     print('<none>')
    # print('Sent parts:     ' + str(sent_parts))
    # print('Received parts: ' + str(received_parts))
    # print('')


file_with_text = open('text.txt', 'r')
text = file_with_text.read()
run(host='localhost', port=8080, debug=True)

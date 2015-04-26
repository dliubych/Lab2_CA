from bottle import *
import bottle


@bottle.get('/scripts/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./scripts/')


@bottle.get('/')
def index():
    return static_file('index.html', root='./')


@get('/workerData')
def worker_get():
    # return "abc"
    return {'n': 4, 'text': 'abba bbbb aaaa  aaaa casd', 'worker_number': 0}


@post('/workerData')
def worker_post():
    worker_number = request.forms.get('worker_number')
    palindromes = request.forms.get('palindromes')

    # Just debugging
    print('I`m worker #%s and I found next palindromes:' % worker_number)
    for i in palindromes.split(','):
        print(i)
    print()


run(host='localhost', port=8080, debug=True)

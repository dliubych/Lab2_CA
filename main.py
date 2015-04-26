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
    return "abcdefg"


run(host='localhost', port=8080, debug=True)


# import cherrypy
# import os.path
#
#
# class Index(object):
# @cherrypy.expose
#     def index(self):
#         return file("index.html")
#
#
# if __name__ == '__main__':
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#
#     conf = {
#         '/': {
#             'tools.sessions.on': True,
#             'tools.staticdir.root': os.path.abspath(os.getcwd())
#         },
#         '/js': {
#             'tools.staticdir.on': True,
#             'tools.staticdir.dir': 'scripts'
#         }
#     }
#
#     cherrypy.quickstart(Index(), '/', conf)

__author__ = 'Maxim'


# import cherrypy
# import os.path
#
#
# class Index(object):
# @cherrypy.expose
#     def index(self):
#         return file("worker.html")
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
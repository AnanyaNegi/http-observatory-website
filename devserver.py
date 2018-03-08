from livereload import Server
from subprocess import call


def regen():
    print('Regenerating via "make publish"')
    call(['make', 'publish'])


server = Server()
server.watch('templates/*', regen, delay=1000)
server.watch('js/*', regen, delay=1000)
server.watch('css/*', regen, delay=1000)

server.serve(root='dist', port=5501, liveport=35729)

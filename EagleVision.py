import http.server
import os
import socketserver
import time
from multiprocessing import Process

from PIL import ImageGrab


def httpserver():
    PORT = 34913
    web_dir = os.path.join(os.path.dirname("./"))
    os.chdir(web_dir)
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("EagleVision is serving at port", PORT)
    httpd.serve_forever()

def EagleVision():
    while True:
        Vision = ImageGrab.grab()
        Vision.save('EagleVision.png')
        time.sleep(10)

if __name__ == '__main__':
    f = open('index.html','wb')
    f.write("<title>EagleVision</title><img src='EagleVision.png' width='1280' height='720'><meta http-equiv='refresh' content='10.0'>".encode())
    f.close()
    os.system('export DISPLAY=:0.0')
    Process(target=httpserver).start()
    Process(target=EagleVision).start()

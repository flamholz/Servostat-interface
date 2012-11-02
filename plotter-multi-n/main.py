from plotter import make_plot
from webserver import MyHandler
from BaseHTTPServer import HTTPServer

import time
import threading
import sys 

UPDATE_PERIOD = 500


class the_plotter_thread(threading.Thread):
    def __init__(self):
        self.go = True
        threading.Thread.__init__(self)
        
    def run(self):
        print 'plotter started'
        while self.go:
            make_plot()
            p = 0
            while (self.go and p<UPDATE_PERIOD):
                p=p+1
                time.sleep(1)
        
        

def main():
    pt = the_plotter_thread()
    pt.start()
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()
        pt.go = False
        

if __name__ == '__main__':
    main()

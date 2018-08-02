#!/usr/bin/env python3.5
from http.server import CGIHTTPRequestHandler, HTTPServer
import base64
import logging
import argparse

requestHandler = CGIHTTPRequestHandler
server = HTTPServer

class AuthHTTPRequestHandler(requestHandler):
    KEY = ''

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def send_authhead(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Security Realm"')
        self.end_headers()

    def do_GET(self):
        authheader = self.headers.get('authorization')
        if self.KEY:
            if authheader is None:
                self.send_authhead()

            elif authheader ==  'Basic ' + self.KEY:
                requestHandler.do_GET(self)

            else:
                self.send_authhead()
                self.wfile.write('Not authenticated')

        else:
            requestHandler.do_GET(self)


def run(port = 8080, host = "", server_class = server, handler_class = AuthHTTPRequestHandler):
    logging.basicConfig(level=logging.INFO)
    serverAddress = (host, port)
    httpd = server_class(serverAddress, handler_class)
    logging.info('Starting server...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping server...\n')

def configServer():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help='set port number (as 8000, etc.)')
    parser.add_argument('--key', help='set username and password as username:password for Base Auth')
    args = parser.parse_args()

    if args.key:
        AuthHTTPRequestHandler.KEY = base64.b64encode(args.key.encode()).decode('ascii')

    run(port= args.port)



      

if __name__ == '__main__':
    configServer()
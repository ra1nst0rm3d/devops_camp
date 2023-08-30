from http.server import BaseHTTPRequestHandler, HTTPServer
from socket import gethostname
from os import getenv
from functools import cached_property
from urllib.parse import urlparse

def get_env(key: str):
    out = getenv(key)
    if out == None:
        return f'Failed to get {key}'
    else:
        return out

class WebRequestHandler(BaseHTTPRequestHandler):
    
    @cached_property
    def url(self):
        return urlparse(self.path)
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        output = ""
        match self.url.path:
            case "/hostname":
                self.wfile.write(gethostname().encode())
                return
            case "/id":
                self.wfile.write(get_env("UUID").encode())
                return
            case "/author":
                self.wfile.write(get_env("AUTHOR").encode())
            case _:
                self.wfile.write("You hit wrong path!".encode())
                return
        return
        
        
if __name__ == '__main__':
    server = HTTPServer(("0.0.0.0",8000), WebRequestHandler)
    server.serve_forever()

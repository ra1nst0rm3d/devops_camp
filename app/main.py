from http.server import BaseHTTPRequestHandler, HTTPServer
from socket import gethostname
from os import getenv
from functools import cached_property
from urllib.parse import urlparse

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
                output = gethostname()
            case "/id":
                output = getenv("UUID")
                if output == None:
                    self.wfile.write("Failed to get UUID!".encode())
                    return
            case "/author":
                output = getenv("AUTHOR")
                if output == None:
                    self.wfile.write("Failed to get author!".encode())
                    return
            case _:
                self.wfile.write("You hit wrong path!".encode())
                return
        self.wfile.write(output.encode())
        return
        
        
if __name__ == '__main__':
    server = HTTPServer(("0.0.0.0",8000), WebRequestHandler)
    server.serve_forever()
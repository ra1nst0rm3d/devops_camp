from http.server import BaseHTTPRequestHandler, HTTPServer
from os import getenv, uname
from functools import cached_property
from urllib.parse import urlparse
from uuid import UUID

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
        match self.url.path:
            case "/hostname":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(uname()[1].encode())
            case "/id":
                # Check UUID for UUIDv4
                uuid = get_env("UUID")
                try:
                    UUID(str(uuid), version=4)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(uuid.encode())
                except ValueError:
                    self.send_response_only(409)
                    self.end_headers()
            case "/author":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(get_env("AUTHOR").encode())
            case _:
                self.send_response(400)
                self.end_headers()
                self.wfile.write("You hit wrong path!".encode())
        
        return
        
        
if __name__ == '__main__':
    server = HTTPServer(("0.0.0.0",8000), WebRequestHandler)
    server.serve_forever()

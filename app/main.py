from flask import Flask,abort
from socket import gethostname
from os import getenv

app = Flask(__name__)

@app.route("/hostname", methods=['GET'])
def index_hostname():
    hostname = gethostname()
    if hostname == None:
        abort(404, "Failed to get hostname")
    else:
        return hostname

@app.route("/author", methods=['GET'])
def index_author():
    author = getenv("AUTHOR")
    if author == None:
        abort(404, "Failed to get author!")
    else:
        return author

@app.route("/id", methods=['GET'])
def index_uuid():
    uuid = getenv("UUID")
    if uuid == None:
        abort(404, "Failed to get UUID!")
    else:
        return uuid

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
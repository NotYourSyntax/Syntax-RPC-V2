from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Syntax RPC running"

def SyntaxHandle():
    server = Thread(target=lambda: app.run(host="0.0.0.0", port=8000))
    server.daemon = True
    server.start()
# MADE BY SYNTAX X GHOSTY
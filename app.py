from flask import Flask
from morse_socket.msocket import config_morse_socket
from routes.routes import morse_api, handle_error_routes


app = Flask(__name__)
app.register_blueprint(morse_api)

handle_error_routes(app)
ws = config_morse_socket(app)

if __name__ == '__main__':
    ws.run(app, debug=False)

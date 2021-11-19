from flask import Flask
from flask_socketio import SocketIO, emit
from resources.constants import SOCKET_CONNECTED, WELLCOME_MESSAGE
from routes.routes import morse_api
from resources.morse_interpreter import Interpreter


app = Flask(__name__)
app.register_blueprint(morse_api)

ws = SocketIO(app, async_mode=None)


@ws.on('morseEvt', namespace='/morse')
def receive_message(message):
    if message['data'] == SOCKET_CONNECTED:
        emit('morseEvtResponse', {'data': WELLCOME_MESSAGE})
    else:
        emit('morseEvtResponse', {'data': Interpreter.text(message['data'])})


if __name__ == '__main__':
    ws.run(app, debug=False)

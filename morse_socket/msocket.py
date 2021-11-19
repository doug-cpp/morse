from flask_socketio import SocketIO, emit
from resources.constants import SOCKET_CONNECTED, WELLCOME_MESSAGE
from resources.morse_interpreter import Interpreter


def config_morse_socket(app):

    ws = SocketIO(app, async_mode=None)

    @ws.on('morseEvt', namespace='/morse')
    def receive_message(message):
        if message['data'] == SOCKET_CONNECTED:
            emit('morseEvtResponse', {'data': WELLCOME_MESSAGE})
        else:
            emit('morseEvtResponse', {'data': Interpreter.text(message['data'])})

    return ws

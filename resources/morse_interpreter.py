from resources.constants import MORSE_DICT, ERROR_MESSAGE


class Interpreter:

    @staticmethod
    def text(morse_code):
        try:
            interpreted = ''
            morse_arr = morse_code.split(' ')
            for morse_item in morse_arr:
                interpreted = interpreted + MORSE_DICT[morse_item]
            return interpreted

        except Exception:
            return ERROR_MESSAGE

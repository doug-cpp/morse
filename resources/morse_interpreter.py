from resources.constants import MORSE_DICT, ERROR_MESSAGE


class Interpreter:

    @staticmethod
    def text(morse_code):
        try:
            interpreted = ''
            morse_arr = morse_code.split(' ')
            for morse_item in morse_arr:
                if morse_item not in MORSE_DICT:
                    raise ValueError(morse_item + ' não é um código válido')

                interpreted = interpreted + MORSE_DICT[morse_item]
            return interpreted

        except ValueError as e:
            return str(e)

        except Exception:
            return ERROR_MESSAGE

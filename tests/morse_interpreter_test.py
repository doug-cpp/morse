import unittest

from resources.morse_interpreter import Interpreter


class TestInterpreter(unittest.TestCase):
    def test_interpreter_ok(self):
        result = Interpreter.text('.- -... -.-. -.. .')
        self.assertEqual(result, 'ABCDE')

    def test_interpreter_fail(self):
        result = Interpreter.text('.- -... -.-. -.. .')
        self.assertEqual(result, '12345')


if __name__ == '__main__':
    unittest.main()
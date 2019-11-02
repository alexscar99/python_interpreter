from interpreter.interpreter import Interpreter


def s():
    a = 1
    b = 2
    print(a + b)


# a friendly compiler transforms `s` into:
what_to_execute = {
    'instructions': [('LOAD_VALUE', 0),
                     ('STORE_NAME', 0),
                     ('LOAD_VALUE', 1),
                     ('STORE_NAME', 1),
                     ('LOAD_NAME', 0),
                     ('LOAD_NAME', 1),
                     ('ADD_TWO_VALUES', None),
                     ('PRINT_ANSWER', None)],
    'numbers': [1, 2],
    'names': ['a', 'b']
}


interpreter = Interpreter()
interpreter.execute(what_to_execute)

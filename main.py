from interpreter.interpreter import Interpreter

what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),  # the first number
                     ("LOAD_VALUE", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [7, 5]}

interpreter = Interpreter()
interpreter.run_code(what_to_execute)

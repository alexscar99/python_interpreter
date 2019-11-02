class Interpreter:

    def __init__(self):
        self.stack = []
        self.environment = {}

    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val

    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)

    def LOAD_VALUE(self, num):
        self.stack.append(num)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def parse_argument(self, instruction, arg, what_to_execute):
        """ Understand what the argument to each instruction means. """
        nums = ['LOAD_VALUE']
        names = ['LOAD_NAME', 'STORE_NAME']

        if instruction in nums:
            arg = what_to_execute['numbers'][arg]
        elif instruction in names:
            arg = what_to_execute['names'][arg]

        return arg

    def execute(self, what_to_execute):
        instructions = what_to_execute['instructions']
        for each_step in instructions:
            instruction, arg = each_step
            arg = self.parse_argument(instruction, arg, what_to_execute)
            bytecode_method = getattr(self, instruction)
            if arg is None:
                bytecode_method()
            else:
                bytecode_method(arg)

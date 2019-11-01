class Interpreter:

    def __init__(self):
        self.stack = []

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

    def run_code(self, what_to_execute):
        instructions = what_to_execute['instructions']
        nums = what_to_execute['numbers']
        for each_step in instructions:
            instruction, arg = each_step
            if instruction == 'LOAD_VALUE':
                num = nums[arg]
                self.LOAD_VALUE(num)
            elif instruction == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()
            elif instruction == 'PRINT_ANSWER':
                self.PRINT_ANSWER()

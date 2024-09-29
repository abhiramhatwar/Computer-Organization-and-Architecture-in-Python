class Register:
    def __init__(self):
        self.registers = [0] * 8

    def load(self, register_index, value):
        if 0 <= register_index < len(self.registers):
            self.registers[register_index] = value

    def move(self, source_index, dest_index):
        if 0 <= source_index < len(self.registers) and 0 <= dest_index < len(self.registers):
            self.registers[dest_index] = self.registers[source_index]

    def display(self):
        return self.registers

reg = Register()
reg.load(0, 10)
reg.load(1, 20)
reg.move(0, 2)
print(reg.display())

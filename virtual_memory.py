class VirtualMemory:
    def __init__(self, size):
        self.memory = [None] * size
        self.page_table = {}

    def load_page(self, page_number, frame_number):
        self.page_table[page_number] = frame_number
        self.memory[frame_number] = f"Page {page_number}"

    def access_memory(self, page_number):
        if page_number in self.page_table:
            return f"Accessing Frame: {self.page_table[page_number]}"
        else:
            return "Page Fault"

vm = VirtualMemory(8)
vm.load_page(1, 2)
print(vm.access_memory(1))
print(vm.access_memory(3))

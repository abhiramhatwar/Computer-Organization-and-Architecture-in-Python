class Pipeline:
    def __init__(self):
        self.stages = ["Fetch", "Decode", "Execute", "Memory", "Write-back"]

    def execute_instruction(self, instruction):
        for stage in self.stages:
            print(f"{instruction} in {stage}")

pipeline = Pipeline()
pipeline.execute_instruction("Instruction 1")

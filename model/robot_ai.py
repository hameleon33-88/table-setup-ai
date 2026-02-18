class TableSetupAI:
    def __init__(self, name="TableSetupAI"):
        self.name = name

    def interpret_task(self, task: str) -> list:
        task = task.lower()

        if "setup the table" in task or "set the table" in task:
            return [
                "Scan dining area",
                "Identify table surface",
                "Place tablecloth",
                "Arrange plates",
                "Arrange cutlery",
                "Place glasses",
                "Finalize table setup"
            ]

        return [
            "Scan environment",
            "Analyze generic task",
            "Execute default routine"
        ]

    def execute_plan(self, steps: list):
        for i, step in enumerate(steps, start=1):
            print(f"[Step {i}] {step}")

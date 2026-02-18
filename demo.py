from model.robot_ai import TableSetupAI

def main():
    task = "Setup the table"

    print("=== Robotics AI Simulator ===")
    print(f"Task received: {task}\n")

    ai = TableSetupAI()
    plan = ai.interpret_task(task)

    print("Execution plan:\n")
    ai.execute_plan(plan)

if __name__ == "__main__":
    main()

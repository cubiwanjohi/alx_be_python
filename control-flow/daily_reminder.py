task = input("Enter your task: ")

# input for priority and time-bound
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# check conditions
match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task} is a low priority task"
    case _:
        reminder = f"{task} has an unspecified priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority in ["high", "medium", "low"]:
        reminder += ". Consider completing it when you have free time."

print(f"Reminder: {reminder}")

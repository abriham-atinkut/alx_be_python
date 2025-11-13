# first decraler 3 input qestions/prompt that asks user
#  - Enter your task:
#  - Priority (high/medium/low):
#  - Is it time-bound? (yes/no):
# based on priority you use 3 matchcase and  each have 3 if else statement 

task = input("Enter your task: ")
priority  = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time == "yes":
            print(f'"{task}" is a high priority task that requires immediate attention today!')
        elif time == "no":
            print(f'"{task}" is a high priority. Consider completing it when you have free time.')
    case "medium":
        if time == "yes":
            print(f'"{task}" is a medium priority task that requires attention today or tommorrow!')
        elif time == "no":
            print(f'"{task}" is a medium priority. Consider completing it when you have free time.')
    case "low":
        if time == "yes":
            print(f'"{task}" is a low priority task that do not requires immediate attention today!. You can do it next weeek.')
        elif time == "no":
            print(f'"{task}" is a low priority. Do not need completing it.')
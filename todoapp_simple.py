
# ***************************
# Simplest To-do App using Python
# ***************************

tasks = []


def add_task():
  task = input("Please enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")


def list_tasks():
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task #{index}. {task}")


def delete_task():
  list_tasks()
  try:
    taskDelete = int(input("Enter the # to delete: "))
    if taskDelete >= 0 and taskDelete < len(tasks):
      tasks.pop(taskDelete)
      print(f"Task {taskDelete} has been removed.")
    else:
      print(f"Task #{taskDelete} was not found.")
  except:
    print("Invalid input.")
    raise


if __name__ == "__main__":
  ### Create a loop to run the app
  print("Welcome to the to do list app :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      add_task()
    elif (choice == "2"):
      delete_task()
    elif (choice == "3"):
      list_tasks()
    elif (choice == "4"):
      break
    else:
      print("Invalid input. Please try again.")

  print("Goodbye 👋👋")
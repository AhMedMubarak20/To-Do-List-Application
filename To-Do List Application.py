tasks = []

while True:
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        task = input("Enter a task: ")
        tasks.append(task)
    elif choice == 2:
        print("Tasks:")
        for task in tasks:
            print(task)
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

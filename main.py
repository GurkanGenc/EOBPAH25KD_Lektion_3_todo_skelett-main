import todo as td

def list_todo_menu():
    while True:
        print("1. List all")
        print("2. List by done")
        print("3. List by priority")
        print("0. Go back")

        choice = input("Enter choice: ")

        if choice == "1":
            print(td.print_all_todos())

        elif choice == "2":
            ...

        elif choice == "3":
            filter_by_priority = int(input("Enter priority (1-5): "))
            above = input("Above priority? (y/n): ").lower() == 'y'
            
            print(td.filter_by_priority(filter_by_priority, above))

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

def main():
    print("Welcome to py-fun todos!")

    while True:
        print("1. Create todo")
        print("2. Mark as done")
        print("3. List todo")
        print("4. Delete todo")
        print("0. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            td.create_todo(
                input("Enter task: "),
                int(input("Enter priority (1-5): "))
            )

        elif choice == "2":
            td.mark_todo_done(input("Enter task to mark as done: "))
            print("Todo marked as done." if td.mark_todo_done(input("Enter task to mark as done: ")) else "Task not found.")

        elif choice == "3":
            list_todo_menu()

        elif choice == "4":
            ...

        elif choice == "0":
            print("Thanks for today and good job! Se yoou later!")
            break

        else:
            print("Invalid choice! Try again!")


if __name__ == "__main__":
    main()
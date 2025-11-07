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
            ...

        elif choice == "4":
            ...

        else:
            print("Invalid choice!")

def main():
    print("Welcome to py-fun todos!")

    while True:
        print("1. Create todo")
        print("2. Mark as done")
        print("3. List todo")
        print("4. Delet toto")
        print("0. Quit")

        choice = input("Enter choice")

        if choice == "1":
            ...

        elif choice == "2":
            ...

        elif choice == "3":
            ...

        elif choice == "4":
            ...

        elif choice == "0":
            print("Thanks for today and good job! Se yoou later!")
            break

        else:
            print("Invalid choice! Try again!")


if __name__ == "__main__":
    main()
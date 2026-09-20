import pathlib
import os


def create_file():
    name = input("Enter file name: ")
    path = pathlib.Path(name)
    if path.exists():
        print("File already exists")
        return
    try:
        data = input("Enter data: ")
        with open(path, "w") as file:
            file.write(data)
        print("File created")
    except OSError as e:
        print(f"Could not create file: {e}")


def read_file():
    name = input("Enter file name: ")
    path = pathlib.Path(name)
    if not path.exists():
        print("File does not exist")
        return
    try:
        with open(path, "r") as file:
            print(file.read())
    except OSError as e:
        print(f"Could not read file: {e}")


def update_file():
    name = input("Enter file name: ")
    path = pathlib.Path(name)
    if not path.exists():
        print("File does not exist")
        return
    try:
        with open(path, "r") as file:
            print(file.read())
    except OSError as e:
        print(f"Could not read file: {e}")
        return

    choice = input("Do you want to replace the data? (y/n): ").strip().lower()
    if choice == "y":
        data = input("Enter new data: ")
        try:
            with open(path, "w") as file:
                file.write(data)
            print("Data updated")
        except OSError as e:
            print(f"Could not update file: {e}")
    elif choice == "n":
        print("Data not updated")
    else:
        print("Invalid choice")


def delete_file():
    name = input("Enter file name: ")
    path = pathlib.Path(name)
    if not path.exists():
        print("File does not exist")
        return
    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
    if confirm == "y":
        try:
            os.remove(path)
            print("File deleted")
        except OSError as e:
            print(f"Could not delete file: {e}")
    else:
        print("Delete cancelled")


def main():
    while True:
        print("\npress 1 to create file")
        print("press 2 to read file")
        print("press 3 to update file")
        print("press 4 to delete file")
        print("press 5 to exit")

        raw_choice = input("\nEnter your choice: ").strip()
        if not raw_choice.isdigit():
            print("Invalid choice")
            continue

        choice = int(raw_choice)
        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            update_file()
        elif choice == 4:
            delete_file()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

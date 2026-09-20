import pathlib
import os
def create_file():
        name = input("Enter file name: ")
        path = pathlib.Path(name)
        if not path.exists():
            with open(path,"w") as file:
                   print("File created")
                   data = input("Enter data: ")
                   file.write(data)
        else:
            print("File already exists")

def read_file():
        name = input("Enter file name: ")
        path = pathlib.Path(name)
        if path.exists():
            with open(path,"r") as file:
                data = file.read()
                print(data)
        else:
            print("File does not exist")

def update_file(): 
    name = input("Enter file name: ")
    path = pathlib.Path(name)
    if path.exists():
        with open(path,"r") as file:
            data = file.read()
            print(data)
            question = input("Do you want to replace the data? (y/n)")
            if question == "y":
                data = input("Enter new data: ")
                with open(path,"w") as file:
                    file.write(data)
            elif question == "n":
                print("Data not updated")
            else:
                print("Invalid choice")

def delete_file():  
    name = input("Enter file name: ")
    path = pathlib.Path(name)
    if path.exists():
        os.remove(path)
    else:
        print("File does not exist")

print("press 1 to create file")
print("press 2 to read file")
print("press 3 to update file")
print("press 4 to delete file")
choice = int(input("\nEnter your choice: "))
if choice == 1:
    create_file()
elif choice == 2:
    read_file()
elif choice == 3:
    update_file()
elif choice == 4:
    delete_file()
else:
    print("Invalid choice")
         

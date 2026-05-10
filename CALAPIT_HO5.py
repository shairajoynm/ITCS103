import os

def dream():
    filename = "dream.txt"

    while True:
        print("\n===== DREAMS FILE MANAGER =====\n")
        print("1. Read inspriring messages.")
        print("2. Add a new inspiring message.")
        print("3. Rewrite the entire inspiring message.")
        print("4. Exit the program.")

        choice = input("\nPlease enter your selected number: ")

        if choice == '1':
            print("===== INSPIRING MESSAGES =====")

            if os.path.exists(filename):
                file = open("dream.txt", "r")
                content = file.read()
                file.close()
                print(content)
            else:
                print("File doesn't exist!!!")
            continue
                
        elif choice == "2":
            new_msg = input("Please enter a new inspiring message: ")
            file = open("dream.txt", "a")
            file.write("\n" + new_msg)
            file.close()
            print("\nA new inspirational message has been added to the file!")
            continue

        elif choice == "3":
            print("\nWARNING!!! This will overwrite all of the inspirational messages in your file.")
            warning = input("type YES to continue: ").upper()

            if warning == "YES":
                over = input("Create a new set of inspirational messages: ")
                file = open("dream.txt", "w")
                file.write(over)
                file.close()
                print("File has been overwritten.")
            else:
                print("Action was cancelled..")
            continue
        
        elif choice == "4":
            print("Closing the program...")
            break

        else:
            print("Invalid input, Please try again")
            continue

dream()
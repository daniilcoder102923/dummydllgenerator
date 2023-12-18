import os
import random

def create_dummy_dll(num_files):
    # Get the current directory path
    directory = os.getcwd()

    for i in range(num_files):
        # Prompt the user for the file name
        file_name = input(f"Enter the file name for DLL file #{i+1}: ")
        file_name = os.path.join(directory, f"{file_name}.dll")

        # Generate some dummy content for the DLL file
        dummy_content = f"This is a dummy DLL file #{i+1}"

        # Write the dummy content to the DLL file
        with open(file_name, "w") as file:
            file.write(dummy_content)

        print(f"Created {file_name}")

# Prompt the user to enter the number of DLL files to create
num_files = int(input("Enter the number of DLL files to create (up to 20): "))

# Validate the user input
if num_files < 1 or num_files > 20:
    print("Invalid input. Please enter a number between 1 and 20.")
else:
    create_dummy_dll(num_files)

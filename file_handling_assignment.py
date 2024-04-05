# File Handling Assignment - file_handling_assignment.py

# Task 1: File Creation and Writing
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("This is a test file.\n")
        file.write("123456789\n")
    print("File 'my_file.txt' created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Task 2: File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("\nReading from 'my_file.txt':")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Task 3: File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending a new line.\n")
        file.write("Another line appended.\n")
        file.write("789101112\n")
    print("Additional lines appended to 'my_file.txt' successfully.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Task 4: Error Handling is demonstrated in all the above tasks with try, except, and finally blocks.

# Optional: Read and display the file content after appending to demonstrate successful append
try:
    with open("my_file.txt", "r") as file:
        print("\nReading from 'my_file.txt' after appending:")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'my_file.txt' was not found after appending.")
except Exception as e:
    print(f"An error occurred while reading the file after appending: {e}")

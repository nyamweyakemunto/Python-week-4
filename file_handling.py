# Open the file "my_file.txt" in write mode ("w")
with open("my_file.txt", "w") as file:

  # Write three lines of text with mixed content
  file.write("This is the first line of text.\n")
  file.write("The second line contains a number: 42\n")
  file.write("This is the final line, adding some variety!")
  
print("Text file created successfully!")

# Open the file "my_file.txt" in read mode ("r")
with open("my_file.txt", "r") as file: 
  
  # Read the entire contents of the file
    content = file.read()

  # Print the contents to the console
print(content)

# Open the file "my_file.txt" in append mode ("a")
with open("my_file.txt", "a") as file:

  # Append three lines of text to the existing content
  file.write("This is a new line appended to the file.\n")
  file.write("Another line added to the end.\n")
  file.write("And one more line for good measure!")

print("Text appended successfully!")

import os

def process_file(file_path):
  try:
    # Open the file in read mode
    with open(file_path, "r") as file:
      # Read the contents of the file
      content = file.read()
      print(content)

  except FileNotFoundError:
    print(f"File not found: {file_path}")

  except PermissionError:
    print(f"Permission denied for file: {file_path}")

  except Exception as e:
    print(f"An unexpected error occurred: {e}")

  finally:
    # Close the file or perform cleanup actions
    if os.path.exists(file_path):
      print(f"File {file_path} is closed.")

file_path = "my_file.txt"
process_file(file_path)
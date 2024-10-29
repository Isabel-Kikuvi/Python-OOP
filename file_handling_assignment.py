def write_to_file():
  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line.\n")
      file.write("Here's some data: 42\n")
      file.write("Another line of text.\n")
    print("Successfully wrote content to my_file.txt")
  except PermissionError:
    print("Error: Insufficient permissions to write to the file.")
  except Exception as e:
    print(f"An error occurred: {e}")


def read_from_file():
  try:
    with open("my_file.txt", "r") as file:
      content = file.read()
      print(content)
  except FileNotFoundError:
    print("Error: File not found. Please create 'my_file.txt'.")
  except Exception as e:
    print(f"An error occurred while reading: {e}")


def append_to_file():
  try:
    with open("my_file.txt", "a") as file:
      file.write("Adding some more text.\n")
      file.write("Numbers can be appended too: 100\n")
      file.write("This is the final line.\n")
    print("Successfully appended content to my_file.txt")
  except PermissionError:
    print("Error: Insufficient permissions to append to the file.")
  except Exception as e:
    print(f"An error occurred while appending: {e}")


if __name__ == "__main__":

  write_to_file()
  read_from_file()
  append_to_file()
  read_from_file()  
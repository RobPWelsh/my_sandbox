from pathlib import Path

# Path is a class
print(Path)  # <class 'pathlib.Path'>

# Path methods
print(Path.cwd())  # C:\Users\rob.welsh\PycharmProjects\my_sandbox
print(Path.home())  # C:\Users\rob.welsh

home_dir = Path.home()
print(home_dir.exists())  # True
print(home_dir.is_dir())  # True
print(home_dir.is_file()) # False


# Create a Path object, does not create the actual file.
path_object = Path(r"C:\Users\rob.welsh\file.txt")
print(path_object)  # C:\Users\rob.welsh\file.txt
print(path_object.exists())  # False
print(path_object.is_file())  # False


# Joining paths - use to join a directory or file to the Path object. Does not create the directory or file
# Using /
new_dir_object_1 = Path(r"C:\Users\rob.welsh") / "archive_1"
print(new_dir_object_1)  # C:\Users\rob.welsh\archive_1
print(new_dir_object_1.exists())  # False

new_file_object = Path.home() / "archive.txt"
print(new_file_object)  # C:\Users\rob.welsh\archive.txt

new_file_object_2 = new_dir_object_1 / "archive_2.txt"
print(new_file_object_2)  # C:\Users\rob.welsh\archive_1\archive_2.txt

# Using joinpath
new_dir_object_2 = Path.home().joinpath("archive_2")
print(new_dir_object_2)  # C:\Users\rob.welsh\archive_2


# Write a new file to an existing directory
new_file_object_1 = Path.home() / "new_file_1.txt"
with new_file_object_1.open(mode="w") as text_file:
    text_file.write('This is some new text.')
# Read the file created above
with new_file_object_1.open(mode="r") as text_file:
    content = text_file.read()
print(content)  # This is some new text.

# Write a new file to a new sub-directory of home
new_test_dir = Path.home() / "new_dir_test"
new_test_dir.mkdir()  # create the new directory
new_file_object_2 = new_test_dir / "new_file_2.txt"
with new_file_object_2.open(mode="w") as text_file_2:
    text_file_2.write('This is new text for the second text file')


# Current file info
print(Path(__file__))  # C:\Users\rob.welsh\PycharmProjects\my_sandbox\file_system_sandbox.py
print(Path(__file__).parent)  # C:\Users\rob.welsh\PycharmProjects\my_sandbox
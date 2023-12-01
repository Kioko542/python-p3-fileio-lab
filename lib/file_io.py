# file_io.py

def write_file(file_path, file_content):
    with open(file_path, 'w') as file:
        file.write(file_content)

def append_file(file_path, append_content):
    with open(file_path, 'a') as file:
        file.write(append_content)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

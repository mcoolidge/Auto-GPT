import os
import os.path

# Set a dedicated folder for file I/O
working_directory = "auto_gpt_workspace"

# Create the directory if it doesn't exist
if not os.path.exists(working_directory):
    os.makedirs(working_directory)


def safe_join(base, *paths):
    """Join one or more path components intelligently."""
    new_path = os.path.join(base, *paths)
    norm_new_path = os.path.normpath(new_path)

    if os.path.commonprefix([base, norm_new_path]) != base:
        raise ValueError("Attempted to access outside of working directory.")

    return norm_new_path


def read_file(filename):
    """Read a file and return the contents"""
    try:
        filepath = safe_join(working_directory, filename)
        with open(filepath, "r", encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return "Error: " + str(e)


def write_to_file(filename, text):
    """Write text to a file"""
    try:
        filepath = safe_join(working_directory, filename)
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(filepath, "w") as f:
            f.write(text)
        return "File written to successfully."
    except Exception as e:
        return "Error: " + str(e)


def append_to_file(filename, text):
    """Append text to a file"""
    try:
        filepath = safe_join(working_directory, filename)
        with open(filepath, "a") as f:
            f.write(text)
        return "Text appended successfully."
    except Exception as e:
        return "Error: " + str(e)


def delete_file(filename):
    """Delete a file"""
    try:
        filepath = safe_join(working_directory, filename)
        os.remove(filepath)
        return "File deleted successfully."
    except Exception as e:
        return "Error: " + str(e)

def search_files(directory):
    found_files = []

    if directory == "" or directory == "/":
        search_directory = working_directory
    else:
        search_directory = safe_join(working_directory, directory)

    for root, _, files in os.walk(search_directory):
        for file in files:
            if file.startswith('.'):
                continue
            relative_path = os.path.relpath(os.path.join(root, file), working_directory)
            found_files.append(relative_path)

    return found_files

def list_files(directory):
    found_files = []

    if directory == "" or directory == "/":
        search_directory = working_directory
    else:
        search_directory = safe_join(working_directory, directory)

    for root, _, files in os.walk(search_directory):
        for file in files:
            if file.startswith('.'):
                continue
            found_files.append(file)

    return found_files

def list_directories(directory):
    found_directories = []

    if directory == "" or directory == "/":
        search_directory = working_directory
    else:
        search_directory = safe_join(working_directory, directory)

    for root, directories, _ in os.walk(search_directory):
        for directory in directories:
            if directory.startswith('.'):
                continue
            found_directories.append(directory)

    return found_directories

def create_directory(directory):
    try:
        directory_path = safe_join(working_directory, directory)
        os.makedirs(directory_path)
        return "Directory created successfully."
    except Exception as e:
        return "Error: " + str(e)
    
def delete_directory(directory):
    try:
        directory_path = safe_join(working_directory, directory)
        os.rmdir(directory_path)
        return "Directory deleted successfully."
    except Exception as e:
        return "Error: " + str(e)
    
def get_current_directory():
    return working_directory


def rename_file(old_name, new_name):
    try:
        old_path = safe_join(working_directory, old_name)
        new_path = safe_join(working_directory, new_name)
        os.rename(old_path, new_path)
        return "File renamed successfully."
    except Exception as e:
        return "Error: " + str(e)
    
def rename_directory(old_name, new_name):
    try:
        old_path = safe_join(working_directory, old_name)
        new_path = safe_join(working_directory, new_name)
        os.rename(old_path, new_path)
        return "Directory renamed successfully."
    except Exception as e:
        return "Error: " + str(e)
    
def copy_file(old_name, new_name):
    try:
        old_path = safe_join(working_directory, old_name)
        new_path = safe_join(working_directory, new_name)
        os.copyfile(old_path, new_path)
        return "File copied successfully."
    except Exception as e:
        return "Error: " + str(e)
    

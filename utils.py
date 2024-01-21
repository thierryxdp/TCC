import os


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def remove_all_files(folder):
    # Verify that the folder exists
    if os.path.exists(folder):
        # List all files in the folder
        files = os.listdir(folder)
        # Iterate over the files and remove them one by one
        for file in files:
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    # print(f"Removed: {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")
    else:
        print(f"Folder not found: {folder}")


def count_blank_spaces(input_string):
    count = 0
    for char in input_string:
        if char.isspace():
            count += 1
        else:
            break  # Exit the loop when a non-blank space character is encountered
    return count


def getMethodName(function_lines):
    for line in function_lines:
        if ('def' in line):
                return line[line.index(" ") + 1 : line.index("(")]
            
    return function_lines[0]


def remove_adjacent_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i - 1]:
            result.append(lst[i])
    return result
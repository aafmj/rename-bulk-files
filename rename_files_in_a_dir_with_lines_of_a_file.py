import os

def rename_files(file_path, directory_path):
    """
    rename files order by name in the directory with each line of file.
    """
    with open(file_path, 'r') as f_x:
        lines = f_x.readlines()
        lines = [line.strip() for line in lines]

    if len(lines) != len(files):
        print("Number of lines in file doesn't match the number of files in directory.")
        return

    # files = sorted(os.listdir(directory_path), key=lambda x: (len(x), x))
    files = sorted(os.listdir(directory_path))

    for i, file_name in enumerate(files):
        old_path = os.path.join(directory_path, file_name)
        new_path = os.path.join(directory_path, str(i) + " - " + lines[i] +".mp4")
        os.rename(old_path, new_path)
        print(f"Renamed {file_name} to {lines[i]}")

if __name__ == "__main__":
    file_path = "x.txt"
    directory_path = "y"

    # uncomment the next line to active the script.
    # rename_files(file_path, directory_path)
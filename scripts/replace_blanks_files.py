import os

def replace_blank_in_filenames(directory, replacement_char='_'):
    # List all files in the directory
    files = os.listdir(directory)

    for filename in files:
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Replace blanks in filename with the specified character
        new_filename = filename.replace(' ', replacement_char)

        # Rename the file with the new filename
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Example usage
if __name__ == "__main__":
    directory = "path/to/save/audio/"  # Path to the directory containing files

    # Replace blanks with '_' in filenames within the directory
    replace_blank_in_filenames(directory, replacement_char='_')
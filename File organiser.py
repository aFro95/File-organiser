import os
import shutil

def organize_files(source_dir, destination_dir):
    # Create destination directories if they don't exist
    for ext in extensions:
        dir_path = os.path.join(destination_dir, ext)
        os.makedirs(dir_path, exist_ok=True)

    # Iterate through files in the source directory
    for file_name in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir, file_name)

        # If it's a file
        if os.path.isfile(source_file_path):
            # Get the file extension
            _, file_ext = os.path.splitext(file_name)
            file_ext = file_ext.lower()

            # If the extension is recognized, move the file to the corresponding directory
            if file_ext in extensions:
                destination_file_path = os.path.join(destination_dir, file_ext, file_name)
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved {file_name} to {file_ext} folder.")
            else:
                print(f"Skipping {file_name} (Unsupported file type)")

# Source directory to organize
source_directory = "D:\New Folder"
# Destination directory where organized files will be moved
destination_directory = "D:\New Folder"
# List of recognized file extensions
extensions = {
    ".txt": "Text Files",
    ".pdf": "PDF Files",
    ".jpg": "Image Files",
    ".png": "Image Files",
    ".mp4": "Video Files",
    ".mp3": "Audio Files",
    # Add more extensions and corresponding categories as needed
}

organize_files(source_directory, destination_directory)

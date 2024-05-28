# File Organizer

This Python script organizes files in a specified source directory into subdirectories based on their file extensions. The files are moved to corresponding subdirectories in the destination directory.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Setup](#setup)
- [Configuration](#configuration)
- [License](#license)

## Description

The File Organizer script helps you keep your directories tidy by organizing files into subdirectories based on their file extensions. You can define the extensions and their corresponding categories, and the script will move files accordingly.

## Features

- Organize files based on their extensions.
- Create subdirectories for each file type if they do not exist.
- Move files to the corresponding subdirectories.
- Log actions taken for each file.

## Usage

1. **Run the Script**: Execute the Python script to start organizing files:
    ```sh
    python File organizer.py
    ```

2. **Follow the Prompts**: The script will automatically move files from the source directory to the appropriate subdirectories in the destination directory based on their file extensions.

## Setup

1. **Install Python**: Ensure you have Python installed on your system.

2. **Download the Script**: Download the `File organizer.py` script to your local machine.

3. **Set Source and Destination Directories**: Modify the `source_directory` and `destination_directory` variables in the script to specify the directories you want to organize.

4. **Define Extensions**: Update the `extensions` dictionary to include any additional file extensions and their corresponding categories as needed.

## Configuration

Update the following variables in the script as needed:

- **source_directory**: The path to the directory containing files you want to organize.
- **destination_directory**: The path to the directory where organized files will be moved.
- **extensions**: A dictionary mapping file extensions to their corresponding categories. For example:
    ```python
    extensions = {
        ".txt": "Text Files",
        ".pdf": "PDF Files",
        ".jpg": "Image Files",
        ".png": "Image Files",
        ".mp4": "Video Files",
        ".mp3": "Audio Files",
        # Add more extensions and corresponding categories as needed
    }
    ```

## License

This project is licensed under the MIT License.

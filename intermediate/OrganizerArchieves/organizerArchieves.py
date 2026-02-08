# Import the os module
# It is used to interact with the operating system (paths, folders, files)
import os

# Import shutil
# It is used for high-level file operations like moving files
import shutil

# Folder that will be organized
# Change this to the path you want to organize
ORIGIN_FOLDER = 'downloads'

# Dictionary that maps folder names to file extensions
# Each key is a folder name
# Each value is a list of file extensions that belong to that folder
TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []  # Files that do not match any category
}

# Loop through the files inside the origin folder
for file in os.listdir(ORIGIN_FOLDER):

    # Build the full path of the file
    file_path = os.path.join(ORIGIN_FOLDER, file)

    # Ignore directories (we only want files)
    if os.path.isdir(file_path):
        continue

    # Split the file name and its extension
    name, extension = os.path.splitext(file)

    # Loop through the file type mapping
    for folder, extensions in TYPES.items():

        # Check if the file extension matches the current category
        if extension.lower() in extensions:
            
            # Build the destination folder path
            destination_folder = os.path.join(ORIGIN_FOLDER, folder)

            # Create the folder if it does not exist
            os.makedirs(destination_folder, exist_ok=True)

            # Move the file to the destination folder
            shutil.move(file_path, destination_folder)
            break

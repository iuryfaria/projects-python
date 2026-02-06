import os
import shutil

# Folder to be organized
ORIGIN_FOLDER =  'downloads' # Change this to your desired folder path

# Mapping of file extensions to their respective folders
TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []  # For files that don't fit into the above categories
}

# List for folder achieves
for folder in TYPES.keys():
    folder_path = os.path.join(ORIGIN_FOLDER, folder)

    # Ignore folder
    if os.path.isdir(ORIGIN_FOLDER): 
        continue 

    name, extension = os.path.splitext(file)

    for folder, extensions in TYPES.items():
        if extension.lower() in extensions:
            destination_folder = os.path.join(ORIGIN_FOLDER, folder)
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(folder_path, destination_folder)
            break
import os
import shutil


src_dir = '/Users/username/Documents/source_directory'
folder_structure = ['Project1', 'Project2', 'Project3']

file_pattern = '{project_name}_{file_name}'

def create_folder_structure(src_dir, folder_structure):
    """
    Create the folder structure based on the provided list
    """
    for folder in folder_structure:
        folder_path = os.path.join(src_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

def move_files(src_dir, folder_structure):
    """
    Move files from the source directory to their corresponding folders
    """
    for file in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file)
        if os.path.isfile(file_path):
            for folder in folder_structure:
                if file.startswith(folder):
                    folder_path = os.path.join(src_dir, folder)
                    shutil.move(file_path, folder_path)
                    break

def rename_files(src_dir, folder_structure, file_pattern):
    """
    Rename files according to the specified pattern
    """
    for folder in folder_structure:
        folder_path = os.path.join(src_dir, folder)
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            project_name = folder
            file_name = file
            new_file_name = file_pattern.format(project_name=project_name, file_name=file_name)
            os.rename(file_path, os.path.join(folder_path, new_file_name))

create_folder_structure(src_dir, folder_structure)
move_files(src_dir, folder_structure)
rename_files(src_dir, folder_structure, file_pattern)
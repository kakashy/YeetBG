import os

def clean_folder(folder_path: str):
    """
    Deletes all files in the specified folder.
    """
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

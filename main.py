import os

# Define the structure: folders and files inside them
structure = {
    "data": [],
    "notebooks": ["covid_api_analysis.py"],
    "visuals": [],  # Empty folder
    "": ["requirements.txt", "README.md"]  # Root-level files
}

# Loop through the structure
for folder, files in structure.items():
    # Set path: current directory if root-level files
    folder_path = os.getcwd() if folder == "" else os.path.join(os.getcwd(), folder)

    # Create folder if not exists
    os.makedirs(folder_path, exist_ok=True)

    # Create each file inside the folder
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'w') as f:
            f.write(f"# {file} in {'root directory' if folder == '' else folder}")


from pathlib import Path

# Define the template folder path and the destination path
year = 2024
template_folder = Path('./')
destination_path = Path(f'./../{year}')

# Create the destination folders and copy files
for day in range(1, 26):
    # Create the folder name with leading zero if necessary
    folder_name = f'{day:02d}'

    # Create the destination folder if it doesn't exist
    destination_folder = destination_path / folder_name
    destination_folder.mkdir(parents=True, exist_ok=True)

    # Copy files from the template folder to the destination folder
    for source_file in template_folder.iterdir():
        if source_file.is_file() and source_file.name in ('main.py', 'input.txt'):
            destination_file = destination_folder / f"{source_file.stem}_{day:02d}{source_file.suffix}"
            destination_file.write_bytes(source_file.read_bytes())
            print(f'File {source_file.name} copied to folder {folder_name}')

print('All files copied successfully.')
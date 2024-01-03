
from pathlib import Path
from typing import Dict
import shutil

def replace_whitespace(filename: str) -> str:
    return filename.replace(' ', '-').replace("---", "-").replace("--", "-").lower()

def update_markdown_links(content: str, mapping: Dict[str, str]) -> str:
    for old_name, new_name in mapping.items():
        content = content.replace(old_name, new_name)
    return content

def copy_and_rename_files(source_folder: Path, destination_folder: Path) -> None:
    name_mapping = {}
    destination_folder.mkdir(parents=True, exist_ok=True)
    print(f"Copying and renaming files from '{source_folder}' to '{destination_folder}'...")
    for file_path in source_folder.rglob('*.md'):
        new_filename = replace_whitespace(file_path.name)
        if new_filename != file_path.name:
            name_mapping[file_path.name] = new_filename
            print(f"Renaming '{file_path.name}' to '{new_filename}'")
        shutil.copy2(file_path, destination_folder / new_filename)

    print("Updating markdown links in files...")
    for file_path in destination_folder.rglob('*.md'):
        with file_path.open('r', encoding='utf-8') as f:
            content = f.read()
        updated_content = update_markdown_links(content, name_mapping)
        with file_path.open('w', encoding='utf-8') as f:
            f.write(updated_content)
    print("All markdown links have been updated.")

if __name__ == "__main__":
    source_folder =      Path(r"C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\notes\JonsCrazyOutline")
    destination_folder = Path(r"C:\Users\jonma\github_repos\jonmatthis\LaserSkeletonsR01\notes\JonsCrazyOutline_no_spaces")
    destination_folder.mkdir(parents=True, exist_ok=True)
    if source_folder.is_dir():
        copy_and_rename_files(source_folder, destination_folder)
        print("File copying and renaming complete.")
    else:
        print(f"The provided source folder path '{source_folder}' does not exist.")

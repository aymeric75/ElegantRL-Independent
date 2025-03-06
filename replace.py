import os
import re

PROJECT_DIR = "elegantrl"
IMPORT_STATEMENT = "from typing import List"

def update_python_files(root_dir):
    """Replace `list[` with `List[` and add `from typing import List` if needed."""
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(foldername, filename)

                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.readlines()

                    modified = False
                    new_content = []

                    # Ensure import statement is added if List[ is used
                    if any("list[" in line for line in content):
                        if not any("from typing import List" in line for line in content):
                            new_content.append(IMPORT_STATEMENT + "\n")
                        new_content.extend(content)
                        modified = True

                    # Replace list[ with List[
                    new_content = [re.sub(r'\blist\[', 'List[', line) for line in new_content]

                    if modified:
                        with open(file_path, "w", encoding="utf-8") as file:
                            file.writelines(new_content)
                        print(f"✅ Updated: {file_path}")

                except Exception as e:
                    print(f"❌ Failed to update {file_path}: {e}")

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR):
        print(f"Error: Directory '{PROJECT_DIR}' not found!")
    else:
        update_python_files(PROJECT_DIR)
        print("🎉 All files updated successfully!")

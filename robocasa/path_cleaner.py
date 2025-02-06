import os

def update_xml_paths(directory, old_path, new_path):
    """
    Traverse through all XML files in the specified directory and its subdirectories,
    replace occurrences of old_path with new_path, and save the modified files.

    Args:
        directory (str): The path to the directory to search.
        old_path (str): The string to search for in the XML files.
        new_path (str): The string to replace the old_path with.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root, file)
                try:

                    # Read the content of the XML file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Replace the old path with the new path
                    updated_content = content.replace(old_path, new_path)

                    # Write the updated content back to the file if changes were made
                    if content != updated_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"Updated file: {file_path}")
                except:
                    print("Error in file: ", file_path)

if __name__ == "__main__":
    # Specify the directory to search
    directory_to_search = input("Enter the directory to search: ").strip()

    # Specify the old and new paths
    old_path_to_replace = "/home/abhiram03/Desktop/mimicgen/robosuite-kitchen/robosuite/models/assets/textures/"
    new_path_to_use = "../../../textures/"

    # Call the function to update paths in XML files
    update_xml_paths(directory_to_search, old_path_to_replace, new_path_to_use)

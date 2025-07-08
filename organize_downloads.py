import os
import shutil

def organize_downloads(downloads_path):
    """
    Organizes files in the specified downloads directory into categorized subfolders.

    Args:
        downloads_path (str): The absolute path to the downloads folder.
    """
    if not os.path.isdir(downloads_path):
        print(f"Error: The path '{downloads_path}' does not exist or is not a directory.")
        return

    print(f"Starting to organize downloads in: {downloads_path}")

    # Define file categories and their corresponding extensions
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic"],
        "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp", ".rtf"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma"],
        "Executables": [".exe", ".msi", ".dmg", ".app", ".deb", ".rpm"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".h", ".sh", ".json", ".xml"],
        "Spreadsheets": [".csv", ".xlsx", ".xls"],
        "Presentations": [".ppt", ".pptx"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "Disk Images": [".iso", ".img"],
        "Torrents": [".torrent"],
        "Virtual Machines": [".ova", ".ovf", ".vmdk", ".vbox"],
        "CAD Files": [".dwg", ".dxf", ".step", ".stp"],
        "GIS Files": [".shp", ".kml", ".geojson"],
        "Ebooks": [".epub", ".mobi", ".azw"],
        "Scripts": [".sh", ".bat", ".ps1"],
        "Configuration Files": [".ini", ".cfg", ".conf"],
        "Log Files": [".log"],
        "Database Files": [".db", ".sqlite", ".sql"],
        "Web Files": [".html", ".css", ".js", ".json", ".xml", ".php", ".asp", ".aspx"],
        "Vector Graphics": [".svg", ".ai", ".eps"],
        "Raster Graphics": [".psd", ".indd", ".ai"], # Some design files
        "Temporary Files": [".tmp", "~"], # Common temporary file extensions/prefixes
    }

    # Create destination folders if they don't exist
    for category_name in file_categories.keys():
        folder_path = os.path.join(downloads_path, category_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

    # Create an 'Others' folder for uncategorized files
    others_folder = os.path.join(downloads_path, "Others")
    if not os.path.exists(others_folder):
        os.makedirs(others_folder)
        print(f"Created folder: {others_folder}")

    # Iterate through all items in the downloads directory
    for item in os.listdir(downloads_path):
        item_path = os.path.join(downloads_path, item)

        # Skip directories and the newly created category folders
        if os.path.isdir(item_path):
            if item in file_categories.keys() or item == "Others":
                continue # Skip the category folders themselves
            else:
                print(f"Skipping directory: {item}")
                continue # Skip other existing subdirectories

        # Get file extension
        _, file_extension = os.path.splitext(item)
        file_extension = file_extension.lower() # Convert to lowercase for case-insensitive matching

        moved = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                destination_folder = os.path.join(downloads_path, category)
                try:
                    shutil.move(item_path, destination_folder)
                    print(f"Moved '{item}' to '{category}'")
                    moved = True
                    break # Move to the next item after successful move
                except shutil.Error as e:
                    print(f"Error moving '{item}' to '{category}': {e}")
                    moved = True # Mark as handled even if error occurred
                except Exception as e:
                    print(f"An unexpected error occurred while moving '{item}': {e}")
                    moved = True
                break # Break from inner loop once category is found

        if not moved:
            # If no category matched, move to 'Others'
            try:
                shutil.move(item_path, others_folder)
                print(f"Moved '{item}' to 'Others'")
            except shutil.Error as e:
                print(f"Error moving '{item}' to 'Others': {e}")
            except Exception as e:
                print(f"An unexpected error occurred while moving '{item}' to 'Others': {e}")

    print("\nDownloads organization complete!")

# --- How to use the script ---
if __name__ == "__main__":
    # IMPORTANT: Replace this with the actual path to your downloads folder.
    # Examples:
    # For Windows: r"C:\Users\YourUsername\Downloads"
    # For macOS/Linux: "/Users/YourUsername/Downloads" or "/home/YourUsername/Downloads"
    # Use 'r' before the string for Windows paths to treat backslashes as literal characters.
    # You can also use os.path.expanduser('~/Downloads') for cross-platform home directory.

    # Example: Auto-detect common downloads paths (adjust as needed)
    # downloads_folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    # You can uncomment the line below and set a specific path if auto-detection doesn't work
    downloads_folder_path = r"C:\Users\Lenovo\Downloads" # Windows example
    # downloads_folder_path = "/Users/YourUsername/Downloads" # macOS/Linux example

    organize_downloads(downloads_folder_path)

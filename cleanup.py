import os
import re
from pathlib import Path
from dotenv import get_key
from datetime import datetime

# Step 1: Retrieve configuration variables using `dotenv.get_key`
config_file = "config.env"
absolute_path = get_key(config_file, "ABSOLUTE_PATH").lower() == "true"
delete_by_date = get_key(config_file, "DELETE_BY_DATE_MODIFIED").lower() == "true"
base_path = get_key(config_file, "PATH")
files_to_keep = int(get_key(config_file, "FILES_TO_KEEP"))
files_pattern = get_key(config_file, "FILES_PATTERN")
log_absolute_path = get_key(config_file, "LOG_ABSOLUTE_PATH").lower() == "true"
log_file_base = get_key(config_file, "LOG_FILE")

# Determine the directory path
if not absolute_path:
    base_path = os.path.join(os.getcwd(), base_path)

base_path = Path(base_path)

# Step 2: Validate the directory
if not base_path.exists() or not base_path.is_dir():
    print(f"Error: Directory '{base_path}' does not exist.")
    exit(1)

# Step 3: Determine log file name and path
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_name = f"{log_file_base}_{current_time}.log"
if not log_absolute_path:
    log_file_name = os.path.join(os.getcwd(), log_file_name)
log_file_path = Path(log_file_name)
log_file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure log directory exists

# Step 4: Find files matching the pattern
pattern = re.compile(files_pattern)
matching_files = [f for f in base_path.iterdir() if f.is_file() and pattern.match(f.name)]

# Step 5: Sort files by modification time
if delete_by_date:
    matching_files.sort(key=lambda x: x.stat().st_mtime)  # Sort by modified time
else:
    matching_files.sort(key=lambda x: x.name) #Sort by Name

# Step 6: Determine files to delete
files_to_delete = matching_files[:-files_to_keep]  # Keep the newest files_to_keep files

# Step 7: Delete the oldest files and log the actions
with open(log_file_path, "w") as log_file:
    log_file.write(f"Log created on: {datetime.now()}\n")
    log_file.write(f"Directory: {base_path}\n")
    log_file.write(f"Files to keep: {files_to_keep}\n")
    log_file.write(f"Matching pattern: {files_pattern}\n")
    log_file.write(f"Sorted by : {'Date Modified' if delete_by_date else 'Name'}\n")
    log_file.write("\nDeleted files:\n")

    # Log deleted files
    for file in files_to_delete:
        log_file.write(f"Deleting: {file}\n")
        print(f"Deleting: {file}")
        file.unlink()

    log_file.write("\nKept files:\n")

    # Log kept files
    files_kept = matching_files[-files_to_keep:]  # Files that are kept
    for file in files_kept:
        log_file.write(f"Kept: {file}\n")
        print(f"Kept: {file}")

    log_file.write("\nFinished. Kept the latest files.\n")


print(f"Finished. Kept the latest {files_to_keep} files.")

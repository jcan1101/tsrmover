import os
import shutil
from tqdm import tqdm

# Define the source and destination folders
source_folder = "C:/Users/Jason_Canfield/Downloads"
destination_folder = os.path.join("C:/Users/Jason_Canfield/Desktop/Review", "TSRs")


# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get the list of all files in the source folder
file_list = os.listdir(source_folder)

# Filter the list for files that match the criteria
filtered_files = [
    filename for filename in file_list
    if filename.endswith(".zip") and "TSR" in filename
]

# Move the files and show progress
for filename in tqdm(filtered_files, desc="Moving files", unit="file"):
    # Build the full paths for the source and destination files
    source_file = os.path.join(source_folder, filename)
    destination_file = os.path.join(destination_folder, filename)

    # Move the file to the destination folder
    shutil.move(source_file, destination_file)

print("File move completed!")


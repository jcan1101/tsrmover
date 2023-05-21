import os
import shutil
import re
from tkinter import Tk, Label, StringVar
from tkinter.ttk import Progressbar

# Define the source and destination folders
source_folder = "C:/Users/Jason_Canfield/Downloads"
destination_folder = os.path.join("C:/Users/Jason_Canfield/Desktop/Review", "TSRs")

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get the list of all files in the source folder
file_list = os.listdir(source_folder)

# Filter the list for files that match the criteria
pattern = re.compile(r"(?i)TSR")  # (?i) enables case-insensitive matching
filtered_files = [
    filename for filename in file_list
    if filename.endswith(".zip") and pattern.search(filename)
]

# Create a GUI window
window = Tk()
window.title("File Move Progress")
window.geometry("400x150")

# Variables to store progress status
progress_var = StringVar()
progress_var.set("0%")

# Label to display progress status
progress_label = Label(window, textvariable=progress_var)
progress_label.pack(pady=10)

# Progress bar
progress_bar = Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Move the files and update progress
total_files = len(filtered_files)
for i, filename in enumerate(filtered_files, start=1):
    # Build the full paths for the source and destination files
    source_file = os.path.join(source_folder, filename)
    destination_file = os.path.join(destination_folder, filename)

    # Move the file to the destination folder
    shutil.move(source_file, destination_file)

    # Update progress variables
    progress_percent = int((i / total_files) * 100)
    progress_var.set(f"{progress_percent}%")
    progress_bar["value"] = progress_percent
    window.update()

# Close the GUI window
window.destroy()

print("File move completed!")
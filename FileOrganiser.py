import os
from pathlib import Path

# this is a list of file formats that the function will check 
directoryList = {
  "Images_Folder" : [".jpg", ".jpeg", ".gif", ".png"],
  "Video_folder": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv"],
  "Zip_Folder": [".iso", ".dmg", ".7z", ".rz", ".gz", ".tar", ".rar", ".zip"],
  "Music_Folder": [".mp3", ".msv", ".wav", ".wma"],
  "PDF_Folder": [".pdf"],
  "EXE_Folder": [".exe", ".msi"],
  "Documents_Folder": [".doc", ".docx"],
}

# i barly understand this. so ignor it
File_Format_Dictionary = { 
  final_file_format: directory
  for directory, file_format_stored in directoryList.items()
  for final_file_format in file_format_stored
  }

# the function
def sortFiles():
  # the loop, well it loops through any items in the directory you are using until all have been sorted.
  # basicly entry is a list of items in the directory
  for entry in os.scandir():
    if entry.is_dir():
      continue
    file_path = Path(entry)
    file_format = file_path.suffix.lower()

    # checks to see if directory exists first and if not creates it
    # then moves the file formats into the corect directory 
    if file_format in File_Format_Dictionary:
      directory_path = Path(File_Format_Dictionary[file_format])
      os.makedirs(directory_path, exist_ok=True)
      os.rename(file_path, directory_path.joinpath(file_path))
    
    # if the file format is not in the dictionary this bit of code will check if "Other_Folder" exists and if not will create it
    # second part moves the file into the new directory
    else:
      otherFolder = "Other_Folder"
      os.makedirs(otherFolder, exist_ok=True)
      os.rename(os.getcwd() + '/' + str(file_path), os.getcwd() + '/' + otherFolder + '/' + str(file_path))

if __name__ == "__main__":
  sortFiles()
from pathlib import Path
import datetime

root_dir = Path('ex2')

file_paths = root_dir.glob('**/*') #python goes inside subfolders


for path in file_paths:
    if path.is_file(): #only for files and not for folders
        time_epoch = path.stat().st_atime
        time = datetime.datetime.fromtimestamp(time_epoch).strftime('%c')
        new_filename = str(time)+'-'+path.name #build a new filename
        new_filepath = path.with_name(new_filename) #build a new path with that file name
        path.rename(new_filepath) #use the new path to rename the previous one
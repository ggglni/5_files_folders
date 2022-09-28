from pathlib import Path

root_dir = Path('files')
# file_paths = root_dir.iterdir()

file_paths = root_dir.glob('**/*') #python goes inside subfolders

# for path in file_paths: #files level
#     for filepath in path.iterdir(): #november and december level
#         print(filepath) #individual files level

for path in file_paths:
    if path.is_file(): #only for files and not for folders
        parent_folder = path.parts[1] #extract parent name
        new_filename = parent_folder+'-'+path.name #build a new filename
        new_filepath = path.with_name(new_filename) #build a new path with that file name
        path.rename(new_filepath) #use the new path to rename the previous one
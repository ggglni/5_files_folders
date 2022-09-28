from pathlib import Path

root_dir = Path('ex1')
# file_paths = root_dir.iterdir()

file_paths = root_dir.glob('**/*') #python goes inside subfolders


for path in file_paths:
    if path.is_file(): #only for files and not for folders
        print(path.parts)
        gp_name = path.parts[1]
        parent_name = path.parts[-2]
        new_filename = gp_name+'-'+parent_name+'-'+path.name #build a new filename
        new_filepath = path.with_name(new_filename) #build a new path with that file name
        path.rename(new_filepath) #use the new path to rename the previous one
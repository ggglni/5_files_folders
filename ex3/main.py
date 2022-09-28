from pathlib import Path

root_dir = Path('files')

file_paths = root_dir.glob('**/*')

for path in file_paths:
    print(path.parts)
    print(path.suffix)
    new_suffix = '.csv'
    new_filepath = path.with_suffix(new_suffix)
    path.rename(new_filepath)
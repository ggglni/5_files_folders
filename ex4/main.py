from logging import root
from pathlib import Path
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path,'w') as zf:
    for path in root_dir.rglob('*.txt'):
        zf.write(path) #write path file to archive
        path.unlink() #delete file
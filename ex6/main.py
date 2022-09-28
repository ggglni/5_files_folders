from pathlib import Path

root_dir = Path('.')
search_term = 'Uniswap'


for path in root_dir.glob('*'):
    if search_term in path.stem:
        print(path.absolute())
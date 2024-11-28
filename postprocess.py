from pathlib import Path
import shutil

docs_path = Path('docs')
try:
    shutil.rmtree(docs_path)
except FileNotFoundError:
    pass

source_path = Path('build/html')
source_path.rename('docs')

build_path = Path('build')
shutil.rmtree(build_path)
from pathlib import Path 

docs_path = Path('docs')
docs_path.rmdir()

source_path = Path('build/html')
source_path.rename('docs')

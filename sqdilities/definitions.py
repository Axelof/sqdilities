from pathlib import Path

library_directory = Path(__file__).parent
files_directory = library_directory / "files"

if not files_directory.exists():
    files_directory.mkdir()

geo_file = files_directory / "geo.mmdb"

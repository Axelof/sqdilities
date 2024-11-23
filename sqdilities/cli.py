import sys
from urllib import request

from sqdilities.definitions import geo_file


CHUNK_SIZE = 1024 * 8


def install_geo(force: bool = False):
    if geo_file.exists() and not force:
        return "Geo file is already installed."

    print("Downloading geo file...")

    with open(geo_file, "wb") as f:
        with request.urlopen("https://sqd.su/geo") as response:
            downloaded = 0
            finished = False
            size = int(response.getheader('Content-Length'))

            while not finished:
                chunk = response.read(CHUNK_SIZE)
                if not chunk:
                    finished = True

                downloaded += len(chunk)

                percent = (downloaded / size) * 100
                sys.stdout.write(f"\rDownloaded {downloaded / 1000000:5.2f} megabytes ({percent:5.2f}%)")
                sys.stdout.flush()

                f.write(chunk)

    return "\rGeo file has been downloaded successfully."


def update_geo():
    file = request.urlopen("https://sqd.su/geo")
    size = int(file.getheader('Content-Length'))

    if not geo_file.exists():
        return "Geo file is not installed."

    if geo_file.exists() and geo_file.stat().st_size == size:
        return "Geo file is up-to-date."

    if not geo_file.exists():
        install_geo(force=True)


def main():
    command = " ".join(sys.argv[1:])

    if command == "install geo":
        print(install_geo())

    if command == "update geo":
        print(update_geo())


if __name__ == "__main__":
    main()

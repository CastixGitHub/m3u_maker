# m3u maker
## Installation
This script doesn't have any dependencies except from python, so install python3.6 before.
python2 is not supported
### manual
```bash
git clone https://github.com/CastixGitHub/m3u_maker
cd m3u_maker
python m3u_maker.py ~/Music > out.m3u
```
## Help menu
```
usage: 'm3u_maker [-h] [sources [sources ...]]

    Finds music files by extension (flac, ogg, oga, wav, mp3,
    aiff, aif, loss, m4a, aac, alac, mogg, opus. webm, mp4, wma, mpc)
    inside a folders and it's subdirectories, makes a m3u file
    without metadata
    

positional arguments:
  sources     
              Source directories that contains the music
              (subdirectories are included).
              We suggest to use an absolute path for better
              compatibility with players.
              If you want to use relative paths remember that them
              are relative to the location of the output m3u file.
              Defaults to the directory where the script is called
              from (`pwd`).

optional arguments:
  -h, --help  show this help message and exit

    Example Usage:
    python m3u_maker.py ~/Music > out.m3u
    Example with random order without duplicates:
    python m3u_maker.py ~/Music | uniq | shuf > out.m3u
```
## Testing & Development

install the project with
```bash
pip install -e '.[test]'
```
run the tests with
```bash
pytest --cov=.
```

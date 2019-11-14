"""
    This file is part of m3u_maker.

    m3u_maker is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    m3u_maker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with m3u_maker.  If not, see <http://www.gnu.org/licenses/>.

"""

from os import walk, getcwd
import argparse


EXTENSIONS = (
    'flac',
    'ogg',
    'oga',
    'wav',
    'mp3',
    'aiff',
    'aif',
    'loss',
    'm4a',
    'aac',
    'alac',
    'mogg',
    'opus',
    'webm',
    'mp4',
    'wma',
    'mpc',
)

parser = argparse.ArgumentParser(
    prog=''''m3u playlist maker.''',
    description='''
    Finds music files (flac, ogg, oga, wav, mp3, aiff, aif, loss, m4a, aac, alac, mogg, opus. webm, mp4, wma, mpc)
    inside a source folder and it's subdirectories, makes a m3u file WITHOUT METADATA
    ''',
    epilog='''
    Example Usage: python m3u_maker.py --out out.m3u
    ''',
)
parser.add_argument('--source', default=getcwd(), help='''
Source directory that contains the music (subdirectories are included).
We suggest to use an absolute path for better compatibility with players.
If you want to use relative paths remember that them are relative to
the location of the output m3u file.
Defaults to the directory where the script is called from (`pwd`).
''')
parser.add_argument('--out', help='''
Output file where the playlist should be saved.
Remember to give it the m3u extension.
If the file already exists it will be deleted!
''')

args = parser.parse_args()

# prefix for absolute paths
prefix = 'file://' if args.source.startswith('/') else ''


def main():
    with open(args.out, 'w') as out_file:
        for walking in walk(args.source):
            for fname in walking[2]:
                if any([fname.endswith(ext) for ext in EXTENSIONS]):
                    out_file.write(f'{prefix}{walking[0]}/{fname}\n')
                else:
                    print(f'DISCARDED: {prefix}{walking[0]}/{fname}')


if __name__ == '__main__':
    main()

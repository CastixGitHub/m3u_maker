#!/usr/bin/env python3
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

from os import walk, getcwd, path
from sys import stderr, argv
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
    prog=''''m3u_maker''',
    description='''
    Finds music files by extension (flac, ogg, oga, wav, mp3,
    aiff, aif, loss, m4a, aac, alac, mogg, opus. webm, mp4, wma, mpc)
    inside a source folder and it's subdirectories, makes a m3u file
    without metadata
    ''',
    epilog='''
    Example Usage:
    python m3u_maker.py ~/Music > out.m3u
    Example with random order without duplicates:
    python m3u_maker.py ~/Music | uniq | shuf > out.m3u
    ''',
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'sources',
    default=[getcwd()],
    nargs='*',
    help='''
Source directories that contains the music
(subdirectories are included).
We suggest to use an absolute path for better
compatibility with players.
If you want to use relative paths remember that them
are relative to the location of the output m3u file.
Defaults to the directory where the script is called
from (`pwd`).
''')


def main(args):
    """Entry point for m3u_maker"""
    # I needed to reimport it here because of tests... this makes me sad
    from sys import stderr   # pylint: disable=redefined-outer-name,reimported,import-outside-toplevel  # noqa
    args = parser.parse_args(args)
    for source in args.sources:
        if not path.isdir(source):
            print(f'{source} is not a directory', file=stderr)
        source = source.rstrip('/') if source != '/' else '/'

        # prefix for absolute paths
        prefix = 'file://' if source.startswith('/') else ''
        for walking in walk(source):
            for fname in walking[2]:
                if any([fname.endswith(ext) for ext in EXTENSIONS]):
                    print(f'{prefix}{walking[0]}/{fname}')
                else:
                    print(f'DISCARDED: {prefix}{walking[0]}/{fname}', file=stderr)


if __name__ == '__main__':
    args = argv[1:] if argv[0] in ('python', 'python3') else argv
    main(argv[1:])

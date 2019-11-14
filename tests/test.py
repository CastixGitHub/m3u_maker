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

import unittest
from os import system, remove


class TestM3uMaker(unittest.TestCase):
    def tearDown(self):
        remove('out.m3u')

    def test_relative_path(self):
        system('python ../m3u_maker.py --source test_files --out out.m3u')
        with open('out.m3u') as out_file:
            output = out_file.read()
            assert 'test_files/01 ok.mp3' in output, output
            assert 'test_files/02 ok.flac' in output, output
            assert '/test_files/02 ok.flac' not in output, output
            assert 'no.png' not in output, output

    def test_absolute_path(self):
        system('python ../m3u_maker.py --out out.m3u')
        with open('out.m3u') as out_file:
            output = out_file.read()
            assert 'file:///' in output, output
            assert 'test_files/01 ok.mp3' in output, output
            assert 'test_files/02 ok.flac' in output, output
            assert '/test_files/02 ok.flac' in output, output
            assert 'no.png' not in output, output


if __name__ == '__main__':
    unittest.main()

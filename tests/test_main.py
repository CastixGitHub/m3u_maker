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


from m3u_maker import main


def test_default_path(capsys):
    """Current working directory should be used here"""
    main([])
    cap = capsys.readouterr()
    assert 'file:///' in cap.out, cap.out
    assert 'test_files/01 ok.mp3' in cap.out, cap.out
    assert 'test_files/02 ok.flac' in cap.out, cap.out
    assert '/test_files/02 ok.flac' in cap.out, cap.out
    assert 'no.png' not in cap.out, cap.out
    assert 'no.png' in cap.err, cap.err


def test_relative_path(capsys):
    """This test assumes you're running it with ``pytest`` from root directory"""
    main(['tests/test_files'])
    output, error = capsys.readouterr()
    assert 'file://' not in output, output
    assert 'tests/test_files/01 ok.mp3' in output, output
    assert 'tests/test_files/02 ok.flac' in output, output
    assert 'no.png' not in output, output
    assert 'no.png' in error, error


def test_absolute_path(capsys):
    main([__file__.replace('test_main.py', 'test_files')])
    output, error = capsys.readouterr()
    assert 'file:///' in output, output
    assert 'test_files/01 ok.mp3' in output, output
    assert 'test_files/02 ok.flac' in output, output
    assert '/test_files/02 ok.flac' in output, output
    assert 'no.png' not in output, output
    assert 'no.png' in error, error


def test_absolute_path_trailing_slash(capsys):
    main([__file__.replace('test_main.py', 'test_files/')])
    output, error = capsys.readouterr()
    assert 'file:///' in output, output
    assert 'test_files/01 ok.mp3' in output, output
    assert 'test_files/02 ok.flac' in output, output
    assert '/test_files/02 ok.flac' in output, output
    assert 'no.png' not in output, output
    assert 'no.png' in error, error


def test_not_existing_directory(capsys):
    main(['not_here'])
    _, error = capsys.readouterr()
    assert error == 'not_here is not a directory\n'


def test_two_directories(capsys):
    main([
        __file__.replace('test_main.py', ''),
        __file__.replace('test_main.py', '')
    ])
    cap = capsys.readouterr()
    assert cap.out.count('test_files/01 ok.mp3') == 2

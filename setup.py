from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='m3u_maker',
    version='0.0.1',
    description='finds music files in directory and create a m3u playlist',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CastixGitHub/m3u_maker',
    author='Castix',
    author_email='castix@autistici.org',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers, End Users',
        'Topic :: Software Development :: Audio :: Multimedia',
        'License :: OSI Approved :: GPLv3 License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='m3u m3u8 playlist',
    python_requires='>=3.0',
    install_requires=[],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/CastixGitHub/m3u_maker/issues',
        'Source': 'https://github.com/CastixGitHub/m3u_maker',
    },
)

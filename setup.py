import os
from setuptools import setup

setup(
    name = "archive",
    version = "1.0",
    author = "Tamim Wahage",
    author_email = "tamim_jf@yahoo.de",
    description = "Archives files of users from certain groups into specified destination folders",
    license = "GPL",
    packages=['archive'],
    url='https://github.com/twahage/archive',
    download_url='https://github.com/twahage/archive/archive/v1.1.tar.gz',
    entry_points = {
        'console_scripts' : ['archive = archive.archive:main']
    },
    #data_files = [
    #    ('share/applications/', ['twahage-archive.desktop'])
    #],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU General Public License (GPL)"
    ]
)

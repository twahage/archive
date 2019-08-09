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
    entry_points = {
        'console_scripts' : ['archive = archive.archive:main']
    },
    #data_files = [
    #    ('share/applications/', ['twahage-archive.desktop'])
    #],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)"
    ]
)

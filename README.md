# Archive Script
This repository contains a python package, that includes a console script, that can be used to archive files belonging to users of certain groups, which can be specified via parameter.
The package has been developed and tested under Linux/Ubuntu 18.04.

## Installation
You can clone this repository and install the console script as a debian package as follows:

In the root directory execute the following commando to create a  `dist` subdirectory that contains the built **.deb** file.

> python setup.py --command-packages=stdeb.command bdist_deb

To build and also directly install the debian package, perform following commando:

> sudo python setup.py --command-packages=stdeb.command install_deb

Alternatively one can of course install the debian package via the *Software Manager*. 

## Usage
The console script can be used as follows:

> archive --dest="bacup" www-data archivetest

That archives all files of users belonging to the *www-data* or *archivetest* group into to the `bacup` subdirectory (relative paths as well as absolute paths can be used). 
If no source directory via the **--dest** option is specified, the current working directory is being searched recursively instead. 

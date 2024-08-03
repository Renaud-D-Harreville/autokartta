# Overview

Karttapullautin (http://www.routegadget.net/karttapullautin/) is a software that enables to create an orienteering map 
from Lidar data. 

Here, the goal is to automate the download and the use of such software in France area.


# Install

To install this package, you can use the setup.sh script with : 

    chmod +x setup.sh
    ./setup.sh

The script will install 'wine' and create a python environment for the project.
Make sure there were no problem during the installation, then you can activate the environment : 

    source .venv/bin/activate

You are now in the python environment, and you can now use the command line : 

    autokartta


# How to use the script

If you are in the project environment, you can use the `autokartta` command, that will download the laz tiles of a 
predefined area (see the function `test_main` in the file `src/autokartta/map.py`)

You can change the area (make sur it is not too big, because one tile use around one hour of CPU already ! ...) 
by changing the tiles numbers ()
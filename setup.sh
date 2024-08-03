#! /bin/sh

# Start by giving execution rights to that file with :
# chmod +x setup.sh

# Because the script relies on the use of a windows software, we first need to install wine

# Installing wine
sudo apt install wine

# Then, we need to install our python environment :

# This script will create a python3.11 virtual environment,
# then update it and finally install the project in dev mode (-e and [dev] arguments)

rm -rf .venv
python3.11 -m venv .venv --prompt autokartta
source .venv/bin/activate
pip install -U pip setuptools
pip install -e .[dev]

echo "\nInstallation finished !"
echo "\nYou can now activate that environment using : \n'source .venv/bin/activate'\n"

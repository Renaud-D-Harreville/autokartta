from autokartta.las import LasDownloader
from autokartta.map import MapsCreator

from pathlib import Path

x1: int = 988
y1: int = 6443
x2: int = 989  # Included
y2: int = 644  # Included

# Number of CPUs that will be used for the processing. Put -1 to use all the CPUs
max_cpu_workers: int = 4

# The directory where you want the output to be created
output_directory: Path = Path("/home/renaud/projects/perso/autokartta/tests/resources/test-output-dir")


def main():
    las_downloader = LasDownloader(x1, y1, x2, y2)
    maps_creator = MapsCreator(las_downloader, output_directory)
    maps_creator.build(max_worker=max_cpu_workers)


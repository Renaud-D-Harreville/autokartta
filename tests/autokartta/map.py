from pathlib import Path
from autokartta.map import MapsCreator
from autokartta.las import LasDownloader


def test_main():
    las_downloader = LasDownloader(988, 6443, 990, 6445)
    output_directory: Path = Path("/home/renaud/projects/perso/autokartta/tests/resources/test-output-dir")
    maps_creator = MapsCreator(las_downloader, output_directory)
    maps_creator.build(max_worker=4)



# def test_main():
#     las_downloader = LasDownloader(968, 6435, 996, 6456)  # BE CAREFUL : This is a big area !!
#     output_directory: Path = Path("/home/renaud/projects/perso/autokartta/tests/resources/test-output-dir")
#     maps_creator = MapsCreator(las_downloader, output_directory)
#     maps_creator.build(max_worker=4)

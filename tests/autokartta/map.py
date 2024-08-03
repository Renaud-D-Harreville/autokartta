from pathlib import Path
from autokartta.map import MapsCreator, RustMapCreator
from autokartta.las import LasDownloader


def test_main():
    las_downloader = LasDownloader(988, 6443, 990, 6445)
    output_directory: Path = Path("/home/renaud/projects/perso/autokartta/tests/resources/test-output-dir")
    maps_creator = MapsCreator(las_downloader, output_directory)
    maps_creator.build(max_worker=4)


class TestRustMapCreator:

    def test_small_build(self):
        output_directory: Path = Path("/home/renaud/projects/perso/autokartta/tests/resources/outputs/test-small-build")
        las_input_directory: Path = Path("/home/renaud/projects/perso/karttapullautin/in/")
        maps_creator = RustMapCreator(output_directory, las_input_directory)
        maps_creator.build()

    def test_big_build(self):
        output_directory: Path = Path("/home/renaud/projects/perso/autokartta/tests/resources/outputs/test-big-build")
        las_input_directory: Path = Path("/tmp/autokartta-tmp/las_files/5f592b25-f2a2-4ed4-b726-3fd89da81e88/")
        maps_creator = RustMapCreator(output_directory, las_input_directory)
        maps_creator.build()


# def test_main():
#     las_downloader = LasDownloader(968, 6435, 996, 6456)  # BE CAREFUL : This is a big area !!
#     output_directory: Path = Path("/home/renaud/projects/perso/autokartta/tests/resources/test-output-dir")
#     maps_creator = MapsCreator(las_downloader, output_directory)
#     maps_creator.build(max_worker=4)

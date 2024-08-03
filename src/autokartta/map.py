from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from uuid import uuid4
import shutil
import wget
import subprocess

from autokartta.las import LasDownloader


class MapCreator:
    """
    Class allowing to create an orienteering map using the karttapullautin software
    It first creates a temporary working directory where it will run.
    Then, the karttapullautin is using the wine software, so that it could be run on a linux OS
    Finally, only the output directory is saved in a desired directory
    """

    main_tmp_directory: Path = Path("/tmp/autokartta-tmp")
    karttapullautin_template_directory: Path = Path(__file__).parent.parent.parent / "resources" / "karttapullautin-template"

    def __init__(self, las_url: str, output_directory: Path):
        self.las_url: str = las_url
        self.tmp_workdir = self.main_tmp_directory / str(uuid4())
        self.output_directory: Path = output_directory

    @property
    def wine_command(self) -> list[str]:
        pullauta_file: Path = self.tmp_workdir / "pullauta.exe"
        las_file: Path = self.tmp_workdir / "in" / self.las_url.split('/')[-1]
        # return ["wine", "pullauta.exe", las_file.name]
        return ["wine", str(pullauta_file)]

    def download_las_file(self):
        # wget.download(self.las_url, str(self.tmp_workdir))
        wget.download(self.las_url, str(self.tmp_workdir / "in/"))

    def build_tmp_workdir(self):
        self.tmp_workdir.mkdir(parents=True)
        shutil.copytree(self.karttapullautin_template_directory, self.tmp_workdir, dirs_exist_ok=True)

    def clean(self):
        shutil.copytree(self.tmp_workdir / "out", self.output_directory, dirs_exist_ok=True)
        shutil.rmtree(self.tmp_workdir)

    def process_karttapullautin(self):
        print(self.wine_command)
        subprocess.run(args=self.wine_command, cwd=self.tmp_workdir)

    def build(self):
        print("Starting tile with url : ", self.las_url)
        self.build_tmp_workdir()
        try:
            self.download_las_file()
            self.process_karttapullautin()
        except Exception as err:
            print("Cannot process url : ", self.las_url)
            print("Error : ", str(err))
        self.clean()
        print("Finished tile with url : ", self.las_url)


class MapsCreator:

    def __init__(self, las_downloader: LasDownloader, output_directory: Path):
        self.las_downloader: LasDownloader = las_downloader
        self.output_directory: Path = output_directory

    def merge_outputs(self):
        # TODO: merge all of the png to create a big map.
        # For now I use the karttapullautin merge command, but it creates something weird...
        pass

    def build(self, max_worker: int = None):
        with ProcessPoolExecutor(max_workers=max_worker) as e:
            for url in self.las_downloader.urls:
                map_creator = MapCreator(url, self.output_directory)
                e.submit(map_creator.build)
        self.merge_outputs()




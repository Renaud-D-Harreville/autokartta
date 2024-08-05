from pathlib import Path
from uuid import uuid4
import wget


class LasDownloader:

    URL_TEMPLATE = "https://storage.sbg.cloud.ovh.net/v1/AUTH_63234f509d6048bca3c9fd7928720ca1/ppk-lidar/RN/LHD_FXX_<XXXX>_<YYYY>_PTS_O_LAMB93_IGN69.copc.laz"
    WORKING_PATH: Path = Path("/tmp/autokartta-tmp/las_files")

    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1: int = x1
        self.y1: int = y1
        self.x2: int = x2
        self.y2: int = y2

    @staticmethod
    def get_str_coord(coord: int) -> str:
        """
        return the int coordinate with zeros ('0's) before the int if it is less than 4 digits.
        :param coord: the coordinate as an integer
        :return: the str version of that coordinate
        """
        str_coord: str = str(coord)
        zeros = "0" * (4 - len(str_coord))
        str_coord = f"{zeros}{str_coord}"
        return str_coord

    @classmethod
    def get_url(cls, x: int, y: int):
        x_str = cls.get_str_coord(x)
        y_str = cls.get_str_coord(y)
        url = cls.URL_TEMPLATE.replace('<XXXX>', x_str).replace('<YYYY>', y_str)
        return url

    @property
    def urls(self) -> list[str]:
        urls: list[str] = list()
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                urls.append(self.get_url(x, y))
        return urls

    def _create_working_directory(self) -> Path:
        working_directory: Path = self.WORKING_PATH / str(uuid4())
        working_directory.mkdir(parents=True)
        return working_directory

    def download(self) -> Path:
        working_directory: Path = self._create_working_directory()
        for url in self.urls:
            try:
                wget.download(url, str(working_directory))
            except Exception as err:
                print("Cannot download url : ", url)
                print("Error : ", str(err))
        return working_directory


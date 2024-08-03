from autokartta.las import LasDownloader


class TestLasDownloader:

    def test_download(self):
        las_downloader = LasDownloader(983, 6429, 984, 6430)
        las_downloader.download()

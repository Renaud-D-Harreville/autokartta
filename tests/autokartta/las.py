from autokartta.las import LasDownloader


class TestLasDownloader:

    def test_download(self):
        las_downloader = LasDownloader(997, 6407, 997, 6407)
        las_downloader.download()

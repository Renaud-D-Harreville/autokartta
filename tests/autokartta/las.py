from autokartta.las import LasDownloader


class TestLasDownloader:

    def test_download(self):
        las_downloader = LasDownloader(988, 6443, 990, 6445)
        las_downloader.download()

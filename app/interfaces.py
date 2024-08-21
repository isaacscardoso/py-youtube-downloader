from abc import ABC, abstractmethod


class VideoDownloaderInterface(ABC):
    @abstractmethod
    def download_video(self, url: str, output_path: str):
        pass

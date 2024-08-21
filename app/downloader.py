import yt_dlp
from tkinter import messagebox
from interfaces import VideoDownloaderInterface


class YoutubeVideoDownloader(VideoDownloaderInterface):
    def __init__(self, status_label):
        self.status_label = status_label

    def download_video(self, url: str, output_path: str):
        ydl_opts = {
            "outtmpl": f"{output_path}/%(title)s.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "progress_hooks": [self._update_status],
            "noplaylist": True,
            "quiet": False,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self._set_status(f"Baixando vídeo de {url}...")
                ydl.download([url])
            self._set_status(f"Vídeo baixado com sucesso para {output_path}")
        except Exception as e:
            self._set_status(f"Erro: {e}")
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def _update_status(self, d):
        if d["status"] == "downloading":
            self._set_status(f"Baixando... {d.get('_percent_str', '0%')} concluído")
        elif d["status"] == "finished":
            self._set_status("Download concluído, finalizando...")

    def _set_status(self, message: str):
        self.status_label.config(text=message)

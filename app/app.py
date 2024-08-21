import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from downloader import YoutubeVideoDownloader


class YoutubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Downloader de Vídeos do YouTube")

        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self.root, text="URL do Vídeo do YouTube:").grid(
            row=0, column=0, padx=10, pady=5
        )
        tk.Label(self.root, text="Caminho de Saída:").grid(
            row=1, column=0, padx=10, pady=5
        )

        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=5)

        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.grid(row=1, column=1, padx=10, pady=5)

        browse_button = tk.Button(
            self.root, text="Procurar", command=self._browse_output_path
        )
        browse_button.grid(row=1, column=2, padx=10, pady=5)

        self.status_label = tk.Label(self.root, text="Status: Aguardando...")
        self.status_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        download_button = tk.Button(
            self.root, text="Baixar", command=self._start_download_thread
        )
        download_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def _browse_output_path(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder_selected)

    def _start_download_thread(self):
        url = self.url_entry.get().strip()
        output_path = self.output_entry.get().strip() or "."

        if not url:
            messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
            return

        downloader = YoutubeVideoDownloader(self.status_label)
        download_thread = threading.Thread(
            target=downloader.download_video, args=(url, output_path)
        )
        download_thread.start()


if __name__ == "__main__":
    root = tk.Tk()
    app = YoutubeDownloaderApp(root)
    root.mainloop()

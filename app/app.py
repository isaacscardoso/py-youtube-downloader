import threading
from downloader import YoutubeVideoDownloader
from tkinter import (
    messagebox,
    filedialog,
    Tk,
    Label,
    Entry,
    Button,
    Radiobutton,
    StringVar,
    OptionMenu,
)


class YoutubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Downloader de Vídeos do YouTube")

        self.download_format = StringVar(value="mp4")
        self.music_quality = StringVar(value="192")  # Default quality set to 192 kbps
        self.video_quality = StringVar(value="best")  # Default quality set to best

        self._create_widgets()

    def _create_widgets(self):
        Label(self.root, text="URL do Vídeo do YouTube:").grid(
            row=0, column=0, padx=10, pady=5
        )
        Label(self.root, text="Caminho de Saída:").grid(
            row=1, column=0, padx=10, pady=5
        )

        self.url_entry = Entry(self.root, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=5)

        self.output_entry = Entry(self.root, width=50)
        self.output_entry.grid(row=1, column=1, padx=10, pady=5)

        browse_button = Button(
            self.root, text="Procurar", command=self._browse_output_path
        )
        browse_button.grid(row=1, column=2, padx=10, pady=5)

        self.status_label = Label(self.root, text="Status: Aguardando...")
        self.status_label.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        download_button = Button(
            self.root, text="Baixar", command=self._start_download_thread
        )
        download_button.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

        # Radio buttons to select format
        Radiobutton(
            self.root,
            text="Vídeo (MP4)",
            variable=self.download_format,
            value="mp4",
            command=self._toggle_quality_options,
        ).grid(row=2, column=0, padx=10, pady=5)
        Radiobutton(
            self.root,
            text="Música (MP3)",
            variable=self.download_format,
            value="mp3",
            command=self._toggle_quality_options,
        ).grid(row=2, column=1, padx=10, pady=5)

        # OptionMenu to select music quality (initially hidden)
        self.quality_label_music = Label(self.root, text="Qualidade de Música:")
        music_quality_options = ["128", "192", "320"]
        self.quality_menu_music = OptionMenu(
            self.root, self.music_quality, *music_quality_options
        )

        # OptionMenu to select video quality (initially visible)
        self.quality_label_video = Label(self.root, text="Qualidade de Vídeo:")
        video_quality_options = [
            "2160",
            "1440",
            "1080",
            "720",
            "480",
            "360",
            "240",
            "144",
            "best",
        ]
        self.quality_menu_video = OptionMenu(
            self.root, self.video_quality, *video_quality_options
        )

        # Display video quality options by default
        self.quality_label_video.grid(row=3, column=0, padx=10, pady=5)
        self.quality_menu_video.grid(row=3, column=1, padx=10, pady=5)

    def _toggle_quality_options(self):
        if self.download_format.get() == "mp3":
            self.quality_label_video.grid_forget()
            self.quality_menu_video.grid_forget()

            self.quality_label_music.grid(row=3, column=0, padx=10, pady=5)
            self.quality_menu_music.grid(row=3, column=1, padx=10, pady=5)
        else:
            self.quality_label_music.grid_forget()
            self.quality_menu_music.grid_forget()

            self.quality_label_video.grid(row=3, column=0, padx=10, pady=5)
            self.quality_menu_video.grid(row=3, column=1, padx=10, pady=5)

    def _browse_output_path(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, folder_selected)

    def _start_download_thread(self):
        url = self.url_entry.get().strip()
        output_path = self.output_entry.get().strip() or "."

        if not url:
            messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
            return

        downloader = YoutubeVideoDownloader(
            self.status_label,
            self.download_format.get(),
            self.music_quality.get(),
            self.video_quality.get(),
        )
        download_thread = threading.Thread(
            target=downloader.download_video, args=(url, output_path)
        )
        download_thread.start()


if __name__ == "__main__":
    root = Tk()
    app = YoutubeDownloaderApp(root)
    root.mainloop()

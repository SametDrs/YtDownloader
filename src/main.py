from PyQt5 import QtWidgets, uic
from win32ui import MessageBox
from pytube import YouTube
from os import getlogin
from threading import Thread


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        uic.loadUi(f'C:/SD/YtDownloader/interface.ui', self)
        self.indirBtn.clicked.connect(self.download)

    def download(self):
        if self.radioMp3.isChecked():
            Thread(target=self.downloadMp3).start()
        else:
            Thread(target=self.downloadMp4).start()

    def checkQuality(self):
        if self.radio1080.isChecked():
            return '1080p'
        elif self.radio480.isChecked():
            return '480p'
        else:
            return '720p'

    def downloadMp3(self):
        if not str(self.videoUrl.text()).startswith('https://www.youtube.com/watch?v='):
            MessageBox('Lütfen bir video linki girin!',
                       'YouTube Downloader', 0)
            return
        MessageBox('İndirme işlemi başladı!', 'YouTube Downloader', 0)
        yt = YouTube(str(self.videoUrl.text()))
        yt.streams.filter(only_audio=True).first().download(
            filename=f'{yt.title}.mp3', output_path=f'C:/users/{getlogin()}/downloads')
        MessageBox(
            f'İndirme Tamamlandı!\nVideo konumu: C:\\users\\{getlogin()}\\downloads', 'YouTube Downloader', 0)

    def downloadMp4(self):
        if not str(self.videoUrl.text()).startswith('https://www.youtube.com/watch?v='):
            MessageBox('Lütfen bir video linki girin!',
                       'YouTube Downloader', 0)
            return
        MessageBox('İndirme işlemi başladı!', 'YouTube Downloader', 0)
        yt = YouTube(str(self.videoUrl.text()))
        res = self.checkQuality()
        if res == "1080p":
            yt.streams.get_highest_resolution().download(
                filename=f'{yt.title}.mp4', output_path=f'C:/users/{getlogin()}/downloads')
        else:
            yt.streams.filter(res=res).first().download(
                filename=f'{yt.title}.mp4', output_path=f'C:/users/{getlogin()}/downloads')
        MessageBox(
            f'İndirme Tamamlandı!\nVideo konumu: C:\\users\\{getlogin()}\\downloads', 'YouTube Downloader', 0)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self, 'YouTube Downloader', "Çıkmak istediğinize emin misiniz?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            if not type(event) == bool:
                event.accept()
            else:
                exit()
        else:
            if not type(event) == bool:
                event.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

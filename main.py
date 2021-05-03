from PySide2.QtWidgets import *
from ui_main import Ui_Dialog
import sys
from pytube import YouTube


class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Youtube Downloader")
        self.btn_dowloand.clicked.connect(self.yt_downloader)

    def yt_downloader(self):
        video_url = self.lineEdit.text()
        if self.rb_video.isChecked():
            YouTube(video_url).streams.first().download()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Vídeo baixado com sucesso")
            msg.exec_()

        elif self.rb_audio.isChecked():
            YouTube(video_url).streams.filter(only_audio=True).first().download()

            msg= QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Audio baixado com sucesso")
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
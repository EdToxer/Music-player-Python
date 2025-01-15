import os, glob, time, sys, pygame
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from threading import Thread
import math

class MainWindow(QMainWindow):
    end = False
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Music Player")
        self.path = "C:\\Users\\YOUR-USER\\Music\\"
        self.not_switching = False
        self.music_loop = False
        
        #Play/stop
        self.ui.pushButton_3.clicked.connect(self.loading_music)
        #Previous
        self.ui.pushButton_2.clicked.connect(self.progress)
        #Next
        #self.ui.pushButton.clicked.connect()
        
        self.music_collection = []
        pygame.init()
        pygame.mixer.music.set_volume(0.1)
        self.track = 0
        self.load_track()
        self.loading_music()
        self.threading()

    def load_track(self):
        for filename in glob.glob(os.path.join(self.path, '*.mp3')):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                self.music_collection.append(f.name.replace(self.path,""))

    def update_labels(self):
        fullname = self.music_collection[self.track].replace(".mp3","")
        pos = fullname.rfind("-")
        author_name = fullname[0:pos]
        track_name = fullname.replace(author_name,"").replace("-","")
        self.ui.label_3.setText(author_name)
        self.ui.label_2.setText(track_name)

    def loading_music(self):
        if self.not_switching == True:
            self.not_switching = False
            pygame.mixer.music.stop()
            self.track += 1
        self.not_switching = True
        track_name = self.path + self.music_collection[self.track]
        pygame.mixer.music.unload()
        pygame.mixer.music.load(track_name, "mp3")
        pygame.mixer.music.play()
        song_len = pygame.mixer.Sound(track_name).get_length()
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(math.ceil(song_len))
        self.update_labels()
        self.music_loop = True

    def progress(self):
        while self.music_loop:
            time.sleep(.4)
            if pygame.mixer.music.get_pos() != (-1):
                self.ui.progressBar.setValue(pygame.mixer.music.get_pos()/ 1000)
            else:
                self.loading_music()
            if self.end == True:
                self.music_loop = False
                pygame.quit()

    def threading(self):
        t1 = Thread(target=self.progress)
        t1.start()

def game_quit():
    MainWindow.end = True
    sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    if app.exec() == 0:
        game_quit()

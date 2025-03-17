import os, glob, time, sys, pygame
from PySide6.QtWidgets import QApplication, QMainWindow
from music_gui_1 import Ui_MainWindow
import threading
import math
import random


class MainWindow(QMainWindow):
    end = False
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Music Player")

        self.t1 = threading.Thread(target=self.progress)

        self.music_loop = False
        self.path = "C:\\Users\\keshu\\Music\\"
        self.random = False
        self.repeat = False
        self.first_track = True
        #Play/stop
        self.ui.push_Play_Stop.clicked.connect(self.play_stop_track)
        #Previous
        self.ui.push_Back.clicked.connect(self.previous_track)
        #Next
        self.ui.push_Next.clicked.connect(self.next_track)
        #Music_volume
        self.ui.slider_Volume.sliderMoved.connect(self.update_volume)
        #Random
        self.ui.push_Shuffle.clicked.connect(self.update_random)
        #Repeat
        self.ui.push_Repeat.clicked.connect(self.update_repeat)
        
        self.music_collection = []
        self.music_shuffled = []
        pygame.init()
        
        pygame.mixer.music.set_volume(1.0)
        self.track_next = 0
        self.load_path()
        self.load_track()
        self.threading()


    def update_volume(self):
        slider_value = self.ui.slider_Volume.value()
        music_volume = (slider_value - slider_value % 10)  / 10
        pygame.mixer.music.set_volume(music_volume)

    def load_path(self):
        self.ui.slider_Volume.setValue(0)
        for filename in glob.glob(os.path.join(self.path, '*.mp3')):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                self.music_collection.append(f.name.replace(self.path,""))
        self.music_shuffled = list(self.music_collection)
        random.shuffle(self.music_shuffled)

    def update_labels(self, music_collection):
        fullname = music_collection[self.track_next].replace(".mp3","")
        pos = fullname.rfind("-")
        author_name = fullname[0:pos]
        track_name = fullname.replace(author_name,"").replace("-","")
        self.ui.label_Author.setText(author_name)
        self.ui.label_TrackName.setText(track_name)

    def update_repeat(self):
        if self.repeat == True:
            self.repeat = False
        else:
            self.repeat = True

    def update_random(self):
        if self.random == True:
            self.random = False
        else:
            self.random = True

    def update_progress_bar(self, track_name):
        song_len = pygame.mixer.Sound(track_name).get_length()
        self.ui.bar_Music.setMinimum(0)
        self.ui.bar_Music.setMaximum(math.ceil(song_len))

    def load_track(self):
        if self.random == True:
            track_name = self.path + self.music_shuffled[self.track_next]
            pygame.mixer.music.load(track_name, "mp3")
            self.update_progress_bar(track_name)
            self.update_labels(self.music_shuffled)
        else:
            track_name = self.path + self.music_collection[self.track_next]
            pygame.mixer.music.load(track_name, "mp3")
            self.update_progress_bar(track_name)
            self.update_labels(self.music_collection)

    def next_track(self):
        if self.music_loop == True:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            self.music_loop = False
        if self.track_next < len(self.music_collection):
            self.track_next += 1
        self.load_track()
        pygame.mixer.music.play()
        self.music_loop = True

    def play_stop_track(self):
        if self.first_track == True:
            pygame.mixer.music.play()
            self.first_track = False
            self.music_loop = True
        elif self.music_loop == False:
            pygame.mixer.music.unpause()
            self.music_loop = True
        else:
            pygame.mixer.music.pause()
            self.music_loop = False

    def previous_track(self):
        if self.music_loop == True:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            self.music_loop = False
        if self.track_next > 0:
            self.track_next -= 1
        self.load_track()
        pygame.mixer.music.play()
        self.music_loop = True

    def progress(self):
        t1 = threading.current_thread()
        while getattr(t1, "do_run", True):
            if self.music_loop == True:
                if pygame.mixer.music.get_pos() != (-1):
                    self.ui.bar_Music.setValue(pygame.mixer.music.get_pos()/ 1000)
                elif pygame.mixer.music.get_pos() == (-1) and self.repeat == True:
                    pygame.mixer.music.play()
                elif pygame.mixer.music.get_pos() == (-1):
                    self.next_track()
                    pygame.mixer.music.play()
            time.sleep(.4)

    def threading(self):
        self.t1.start()

def game_quit(wind):
    wind.t1.do_run = False
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    if app.exec() == 0:
        game_quit(window)

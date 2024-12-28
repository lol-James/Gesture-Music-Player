import os
import time
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import cv2
from Ui_music import Ui_GestureMusicPlayer
from gesture_analyzer import GestureAnalyzer

class GestureMusicPlayer(QMainWindow, Ui_GestureMusicPlayer):
    def __init__(self):
        # ui initialization
        super().__init__()
        self.window= QMainWindow()
        self.setupUi(self)
        self.show()
        # initialize gesture analyzer and camera frame
        self.gesture_analyzer = GestureAnalyzer()
        self.gesture_analyzer.processed_image_signal.connect(self.update_image)
        self.gesture_analyzer.result_str_signal.connect(self.process_gesture_instruction)
        self.gesture_analyzer.start()
        self.current_instruction = ""
        self.is_rewind_mode = False
        # init music player
        self.current_songs = []
        self.current_selection_song = ""
        self.current_volume = 50
        self.stopped = False
        self.player = QMediaPlayer()
        self.player.setVolume(self.current_volume)
        #init slider timer
        self.timer = QTimer(self)
        self.timer.start(1000)
        # connections
        self.actionAdd_Songs.triggered.connect(self.add_songs)
        self.actionRemove_Selected.triggered.connect(self.remove_one_song)
        self.actionRemove_All.triggered.connect(self.remove_all_songs)
        self.timer.timeout.connect(self.move_slider)
        self.musicSlider.sliderMoved[int].connect(lambda: self.player.setPosition(self.musicSlider.value()))
        self.volumeSlider.valueChanged.connect(self.volume_changed)
        self.playpushButton.clicked.connect(self.play_song)
        self.pausepushButton.clicked.connect(self.toggle_pause)
        self.nextpushButton.clicked.connect(self.next_song)
        self.previouspushButton.clicked.connect(self.previous_song)
        self.stoppushButton.clicked.connect(self.stop_song)
        
    def update_image(self, processed_image):
        rgb_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.camera_label.setPixmap(pixmap)
        
    def process_gesture_instruction(self, gesture_text):
        # self.current_instruction = gesture_text
        if (gesture_text == 'Lotus' or (len(self.current_instruction) > 20 and gesture_text.isdigit() and 1 <= (int(gesture_text)) <= 9)):
            self.is_rewind_mode = True
            
        if len(self.current_instruction) > 20 and self.is_rewind_mode == False:
            self.is_rewind_mode = False
            self.current_instruction = 'Invalid Gesture'
        else:
            self.current_instruction = gesture_text
            if self.current_instruction.isdigit() and 1 <= (num := int(self.current_instruction[0])) <= 9:
                self.current_instruction += '×10s ⏪' if self.is_rewind_mode else "×10s ⏩"
        self.info_textbox.setText(self.current_instruction)
        
        if self.current_instruction == 'ok':
            self.playpushButton.click()
        elif self.current_instruction == '0':
            self.pausepushButton.click()
        elif self.current_instruction == 'Pinky':
            self.stoppushButton.click()
        elif self.current_instruction == 'Lotus':
            self.current_instruction += ": Gesture 1-9, n×10s ⏪"
            self.info_textbox.setText(self.current_instruction)
        elif self.current_instruction[0].isdigit() and 1 <= (num := int(self.current_instruction[0])) <= 9:
            if self.is_rewind_mode:
                self.player.setPosition(max(self.player.position() - 10 * num * 1000, 0))
                self.is_rewind_mode = False
            else:
                self.player.setPosition(min(self.player.position() + 10 * num * 1000, self.player.duration()))
        elif self.current_instruction == 'Up':
            self.volumeSlider.setValue(min(self.volumeSlider.value() + 10, 100))
        elif self.current_instruction == 'Down':
            self.volumeSlider.setValue(max(self.volumeSlider.value() - 10, 0))
        elif self.current_instruction == 'Left':
            self.previous_song()
        elif self.current_instruction == 'Right':
            self.next_song()
        elif self.current_instruction == 'Rock!':
            self.volumeSlider.setValue(100)
                
    def add_songs(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            caption='Add Songs',
            directory='./musics',
            filter='Supported Files (*.mp3;*.mpeg;*.m4a)'
        )
        if files:
            for file in files:
                self.current_songs.append(file)
                self.listWidget.addItem(os.path.basename(file))
                
    def play_song(self):
        try:
            self.stopped = False
            current_index = self.listWidget.currentRow()
            self.current_selection_song = self.current_songs[current_index]
            self.current_song_label.setText(f'Playing {os.path.basename(self.current_selection_song)}...')
            song_url = QMediaContent(QUrl.fromLocalFile(self.current_selection_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f'Playing song Error: {e}')
    
    def move_slider(self):
        if self.stopped:
            return
        elif self.player.state() == QMediaPlayer.PlayingState:
            self.musicSlider.setMinimum(0)
            self.musicSlider.setMaximum(self.player.duration())
            selider_position = self.player.position()
            self.musicSlider.setValue(selider_position)
            current_time = time.strftime('%H:%M:%S', time.gmtime(self.player.position() / 1000))
            song_duration = time.strftime('%H:%M:%S', time.gmtime(self.player.duration() / 1000))
            self.start_time_label.setText(current_time)
            self.end_time_label.setText(song_duration)
            
    def volume_changed(self):
        try:
            self.current_volume = self.volumeSlider.value()
            self.player.setVolume(self.current_volume)
            self.volume_label.setText(f'{self.current_volume}')
        except Exception as e:
            print(f'Changing volume Error: {e}')     
            
    def toggle_pause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        elif self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
    
    def next_song(self):
        try:
            next_index = (self.listWidget.currentRow() + 1) % len(self.current_songs)
            self.listWidget.setCurrentRow(next_index)
            self.current_selection_song = self.current_songs[next_index]
            song_url = QMediaContent(QUrl.fromLocalFile(self.current_selection_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
            self.current_song_label.setText(f'Playing {os.path.basename(self.current_selection_song)}...')
        except Exception as e:
            print(f'Next song Error: {e}')

    def previous_song(self):
        try: 
            previous_index = (self.listWidget.currentRow() - 1) % len(self.current_songs)
            self.listWidget.setCurrentRow(previous_index)
            self.current_selection_song = self.current_songs[previous_index]
            song_url = QMediaContent(QUrl.fromLocalFile(self.current_selection_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
            self.current_song_label.setText(f'Playing {os.path.basename(self.current_selection_song)}...')
        except Exception as e:
            print(f'Previous song Error: {e}')
    
    def stop_song(self):
        try:
            self.player.stop()
            self.current_song_label.setText('Stopped...')
            self.musicSlider.setValue(0)
            self.start_time_label.setText('00:00:00')
            self.end_time_label.setText('00:00:00')
        except Exception as e:
            print(f'Stop song Error: {e}')
            
    def remove_one_song(self):
        current_index = self.listWidget.currentRow()
        self.current_songs.pop(current_index)
        self.listWidget.takeItem(current_index)
    
    def remove_all_songs(self):
        self.current_songs.clear()
        self.listWidget.clear()
        self.stop_song()
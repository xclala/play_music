from sys import exit
from pygame import mixer
import pygame
from win32ui import CreateFileDialog
from win32con import OFN_OVERWRITEPROMPT, OFN_FILEMUSTEXIST

pygame.display.set_mode([300, 300])

dialog = CreateFileDialog(1, None, None,
                          OFN_OVERWRITEPROMPT | OFN_FILEMUSTEXIST,'Music File (*.mp3)|*.mp3|')
dialog.SetOFNInitialDir('')
dialog.DoModal()
music = dialog.GetPathName()
mixer.init()
mixer.music.load(music)
mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

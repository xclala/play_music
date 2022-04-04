from playsound import playsound
from win32ui import CreateFileDialog
from win32con import OFN_OVERWRITEPROMPT, OFN_FILEMUSTEXIST

dialog = CreateFileDialog(1, None, None,
                          OFN_OVERWRITEPROMPT | OFN_FILEMUSTEXIST,'Music File (*.mp3)|*.mp3|')
dialog.SetOFNInitialDir('')
dialog.DoModal()
music = dialog.GetPathName()
playsound(music)
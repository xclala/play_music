try:
    from playsound import playsound
    from tkinter.filedialog import askopenfilename
    playsound(askopenfilename())
except Exception as e:
    print(e)
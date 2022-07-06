import tkinter as tk
import shutil
from tkinter import filedialog



def file_upload():
    root = tk.Tk()
    root.withdraw()

#Prompt for file input

    file_path = filedialog.askopenfile(                            #Does not give clean directory string...
            initialdir = "C:/Users/MainFrame/Desktop/", 
            title = "Open file", 
            filetypes = (("Text Files", "*.txt"),("Image Files", "*.png"),)
            )
            
    #Translate file_path given to correct path name and give string value
    
    file_path_str = str(file_path.name)

    #Copy chosen file to upload folder

    shutil.copy(file_path_str, 'C:/Program Files (x86)/Tier2Tickets/upload')

file_upload()

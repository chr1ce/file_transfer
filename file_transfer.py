import tkinter as tk
import shutil
from tkinter import filedialog

dirs_exist_ok = True #Allows use of existing directory with copy(?)

def file_upload():
    root = tk.Tk()
    root.withdraw()

#Prompt for file input

    file_path = filedialog.askopenfile(                            #Doesn't give clean directory string...
            initialdir = "C:/Users/MainFrame/Desktop/", 
            title = "Open file", 
            filetypes = (("Text Files", "*.txt"),("Image Files", "*.png"),)
            )
    
    #file_path = filedialog.askdirectory() #Does not give specific file choice(?)
            
    #Translate file_path to correct directory name
    
    file_path_dir = file_path.name

    #Copy file(s) to upload folder

    file_path_str = str(file_path_dir) #Gives file_path string value

    #os.chdir(file_path_str) #Not needed

    shutil.copy(file_path_str, 'C:/Program Files (x86)/Tier2Tickets/upload')

file_upload()
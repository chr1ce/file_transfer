import win32gui, win32con, os
import shutil

def file_upload():
    filter = "Text files\0*.txt\0"
    customfilter = "Other file types\0*.*\0"

#Prompt for file input

    file_path, customfilter, flags = win32gui.GetSaveFileNameW(
        InitialDir=os.environ["temp"],
        Flags=win32con.OFN_ALLOWMULTISELECT | win32con.OFN_EXPLORER,
        File="somefilename",
        DefExt="txt",
        Title="GetSaveFileNameW",
        Filter=filter,
        CustomFilter=customfilter,
        FilterIndex=1,
    )
            
    #Translate file_path given to correct path name and give string value
    
    file_path_str = str(file_path)

    #Copy chosen file to upload folder

    shutil.copy(file_path_str, 'C:/Program Files (x86)/Tier2Tickets/upload')

file_upload()

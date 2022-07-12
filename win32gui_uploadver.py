import win32gui, win32con, os
import shutil

def file_upload():
    
#Define file types accepted
    
    filter = "All files\0*.*\0"
    customfilter = "Other file types\0*.*\0"

#Prompt for file input

    file_path, customfilter, flags = win32gui.GetSaveFileNameW(
        InitialDir=os.environ["temp"],
        Flags=win32con.OFN_ALLOWMULTISELECT | win32con.OFN_EXPLORER,
        File="file",
        DefExt="txt",
        Title="GetSaveFileNameW",
        Filter=filter,
        CustomFilter=customfilter,
        FilterIndex=1,
    )
            
    #Give string value to file_path
    
    file_path_str = str(file_path)

    #Copy chosen file to upload folder

    shutil.copy(file_path_str, 'C:/Program Files (x86)/Tier2Tickets/upload')

file_upload()

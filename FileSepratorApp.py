import os
import shutil

extension_dict={
    "audio_extensions":(".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".aiff", ".alac", ".opus"),
    "app_extensions":(".exe", ".msi", ".apk", ".bat", ".jar", ".bin", ".sh", ".deb", ".rpm", ".dmg"),
    "video_extensions":(".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm", ".m4v", ".mpeg", ".3gp"),
    "document_extensions":(".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".odt", ".rtf", ".csv", ".epub"),
    "image_extensions":(".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic", ".ico")
    }
folderpath=input("Enter Folder path:   ")

def ext_finder(folder_path,fileextension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in fileextension:
             if file.endswith(extension):
                 files.append(file)
    return files

for exten_type,extension in extension_dict.items():
   ext_list=ext_finder(folderpath,extension)
   if ext_list:
       foldername=exten_type.split("_")[0]+"_Files"
       folder_path=os.path.join(folderpath,foldername)
       if  not os.path.exists(folder_path):
           os.mkdir(folder_path)
           for item in ext_list:
               file_path=os.path.join(folderpath,item)
               file_new_path=os.path.join(folder_path,item)
               shutil.move(file_path,file_new_path)
                
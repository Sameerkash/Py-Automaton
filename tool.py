# Select the files from the path
# while not stopped,
# Check if the file has already been operated on
#  if the file is Zip or rar format unzip the file
# else if it is a .crdownload, wait to downlaod and unzip file
# else if it is an image, .png, .jpeg, .jpg, put it in images folder
# else if it is a document, .pdf, .docx, .doc .txt, put it in documents folder
# else do nothing


import os
import zipfile
import time
import random

newest = []

# Chnage the path to your desired destination 
#  replcae \\ with / if on Mac or Linux
path = "D:\\Downloads"

#List of old files 
old_files = os.listdir(path)
num_of_old_files = len(old_files)

done = False


def open_folder(folder):
    explorer = os.path.realpath(path+"\\"+folder)
    os.startfile(explorer)


while not done:
    new_files = os.listdir(path)
    no_of_new_files = len(new_files)

    if len(newest) != 0:
        for x in newest:
            if x not in new_files:
                old_files.remove(x)
                num_of_old_files -= 1
                newest.remove(x)

    if no_of_new_files > num_of_old_files:
        time.sleep(2)
        new_files = os.listdir(path)
        count = no_of_new_files - num_of_old_files
        exten = 0
        for i, file in enumerate(old_files):
            if new_files[i+exten] != file:
                extension_list = new_files[i+exten].split(".")
                extension = len(extension_list)
                if new_files[i + exten] != file:
                    #Comparison of zip files to unzip and delete the zip
                    if new_files[i + exten][-4:] == '.zip' or new_files[i + exten][-4:] == '.ZIP' or new_files[i + exten][-4:] == '.rar':
                        try:
                            os.chdir(path)
                            os.mkdir(new_files[i + exten][:-4])
                            obj = zipfile.ZipFile(new_files[i + exten], 'r')
                            obj.extractall(
                                path + '\\' + new_files[i + exten][:-4])
                            obj.close()
                            open_folder(new_files[i + exten][:-4])  # Comment this line to stop the file explorer from opening
                            time.sleep(15)
                            os.remove(path + '\\' + new_files[i + exten]) # Comment this line to remove the unzip folder 

                        except:
                            print(new_files[i + exten])
                    # If new download, add to newest list
                    elif new_files[i + exten][-11:].lower() == '.crdownload':
                        newest.append(new_files[i + exten])
                        
                    # Comapre jpg, png, jprg, webp
                    elif new_files[i + exten][-4:].lower() == '.jpg' or new_files[i + exten][-4:].lower() == '.png':
                        os.replace(
                            path+'\\'+new_files[i + exten], (path+"\\images\\{}"+new_files[i + exten]).format(random.random()))

                    elif new_files[i + exten][-5:].lower() == '.webp' or new_files[i + exten][-4:].lower() == '.jpeg':
                        os.replace(
                            path+'\\'+new_files[i + exten], (path+"\\images\\{}"+new_files[i + exten]).format(random.random()))
                   
                    # Comapre pdf, doc, docx
                    elif new_files[i + exten][-4:].lower() == '.pdf' or new_files[i + exten][-4:].lower() == '.doc' or new_files[i + exten][-5:].lower() == '.docx':
                        os.replace(
                            path+'\\'+new_files[i + exten], (path+"\\Documents\\"+new_files[i + exten]))
                    else:
                        pass
                    exten += 1
                    if exten == count:
                        break
            num_of_old_files = no_of_new_files
            old_files = new_files
    elif no_of_new_files < num_of_old_files:
        num_of_old_files = no_of_new_files
        old_files = new_files
    else:
        pass

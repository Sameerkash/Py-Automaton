
import os, zipfile, time

newest = []
# username = input("Enter your PC-name exactly as it is: ")
path = "D:\\Downloads"
old_files = os.listdir(path)
numof_old_files = len(old_files)

done = False
while not done:
    new_files = os.listdir(path)
    numof_new_files = len(new_files)
    if len(newest) != 0:
        for x in newest:
            if x not in new_files:
                old_files.remove(x)
                numof_old_files -= 1
                newest.remove(x)
    if numof_new_files > numof_old_files:
        time.sleep(2)
        new_files = os.listdir(path)
        count = numof_new_files - numof_old_files
        exten = 0
        for i,file in enumerate(old_files):
            if new_files[i + exten] != file:
                if new_files[i + exten][-4:] == '.zip' or new_files[i + exten][-4:] == '.ZIP':
                    try:
                        os.chdir(path)
                        os.mkdir(new_files[i + exten][:-4])
                        obj = zipfile.ZipFile(new_files[i + exten],'r')
                        obj.extractall(path + '\\' + new_files[i + exten][:-4])
                        obj.close()
                    except:
                        print(new_files[i + exten])
                elif new_files[i + exten][-11:].lower() == '.crdownload':
                    newest.append(new_files[i + exten])
                else:
                    pass
                exten += 1
                if exten == count:
                    break
        numof_old_files = numof_new_files
        old_files = new_files
    elif numof_new_files < numof_old_files:
        numof_old_files = numof_new_files
        old_files = new_files
    else:
        pass
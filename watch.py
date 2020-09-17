# watch for file changes
# if OnCreate Event is invoked, execute a function
# if the file created time is less than 30 mins, add to array.
# if the file is Zip or rar format unzip the file
# else if it is a .crdownload, wait to downlaod and unzip file
# else if it is an image, .png, .jpeg, .jpg, put it in images folder
# else if it is a document, .pdf, .docx, .doc .txt, put it in documents folder
# else do nothing


import watchdog.events
import watchdog.observers
import time
from datetime import datetime, timedelta
import os
import zipfile

path = "D:\\Downloads"


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.png'],
                                                             ignore_directories=True, case_sensitive=False)
        self.last_modified = datetime.now()

# Set the patterns for PatternMatchingEventHandler

    def on_created(self, event):

        print("Watchdog received created event - % s." % event.src_path)

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()
        print(f'Event type: {event.event_type}  path : {event.src_path}')
        print(event.is_directory)  # This attribute is also available

    def open_folder(self, folder):
        explorer = os.path.realpath(path+"\\"+folder)
        os.startfile(explorer)

    def handleFile(self):
        files = os.listdir(path)
        for i, file in enumerate(files):
            extension_list = file[i].split(".")
            extention = len(extension_list)
            if file[i][-4:] == '.zip' or file[i][-4:] == '.ZIP' or file[i][-4:] == '.rar':
                try:
                    os.chdir(path)
                    os.mkdir(file[i][:-4])
                    obj = zipfile.ZipFile(file[i], 'r')
                    obj.extractall(
                        path + '\\' + file[i][:-4])
                    obj.close()
                    # Comment this line to stop the file explorer from opening
                    open_folder(file[i][:-4])
                    time.sleep(15)
                    # Comment this line to remove the unzip folder
                    os.remove(path + '\\' + file[i])

                except:
                    print(file[i])


if __name__ == "__main__":
    src_path = r"D:\\Downloads"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

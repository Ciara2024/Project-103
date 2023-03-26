import os
import shutil
import sys
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/alexa/Downloads"
to_dir = "Document_Files"

list_of_files =  os.listdir(from_dir)
#print(list_of_files)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified")

    def on_moved(self, event):
        print(f"Yay! {event.src_path} has been moved")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

for i in list_of_files:
    files, extention=os.path.splitext(i)
    if extention == "":
        continue
    if extention in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "image_files"
        path3 = to_dir + "/" + "image_files" + '/'+i
        if os.path.exists(path2):
            print("Moving...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving...")
            shutil.move(path1, path3)
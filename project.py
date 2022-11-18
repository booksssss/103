import time
import os
import shutil
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

fromdir = "/Users/nehasharma/Downloads/testt"
todir = "/Users/nehasharma/Downloads/neha"
listOfFiles= os.listdir(fromdir)

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}")
    def on_modified(self, event):
        print(f"Someone modified {event.src_path}")
    def on_moved(self, event):
        print(f"Someone moved {event.src_path}")
                  
            
       

#initialize the event handler class (object)
eventHandler = FileMovementHandler()
#initialize observer
observer = Observer()
#schedule the observer
observer.schedule(eventHandler, fromdir, recursive = True)
#start the observer
observer.start()
try:

    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()      




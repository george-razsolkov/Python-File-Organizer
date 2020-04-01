from watchdog.observers import Observer
from FileHandler import FileEventHander

import time

# TODO ADD CONFIG PARSER AND ADD THESE INTO THE CONFIG
tracked_folder = "${FOLDER TO TRACK FOR FILES}"
files_moved_to = "${FOLDER TO MOVE THE FILES TO AND CREATE SUBDIRS}"
observeRecursive = True

handler = FileEventHander(tracked_folder, files_moved_to)
observer = Observer()
observer.schedule(handler, tracked_folder, recursive=observeRecursive)

print("observation of " + tracked_folder + " starts!")

observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()

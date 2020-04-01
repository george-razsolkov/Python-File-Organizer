from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from manager.FileTypeManager import FileTypeManager

import os
import time
import pprint
import random
import string


class FileEventHander(FileSystemEventHandler):

    i = 1

    def __init__(self):
        self.file_type_manager = FileTypeManager()

    def on_modified(self, event):

        try:
            for filename in os.listdir(tracked_folder):
                src = tracked_folder + "/" + filename

                folder = self.file_type_manager.destination_folder_for_file(src)
                directory = files_moved_to + "/" + folder

                if not os.path.exists(directory):
                    os.makedirs(directory, exist_ok=True)

                new_destination = directory + "/" + filename

                if os.path.exists(new_destination):
                    new_destination = new_destination + "_" + self.randomString(10)

                os.rename(src, new_destination)
        except Exception as e:
            print(e)

    def randomString(self, length):
        letters = string.ascii_lowercase

        return "".join(random.choice(letters) for i in range(length))


# get from config later
tracked_folder = "/home/georgi/personals/from_folder"
# get from config later
files_moved_to = "/home/georgi/personals/to_folder"
# get from config later
observeRecursive = True

# move this section to main
handler = FileEventHander()
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

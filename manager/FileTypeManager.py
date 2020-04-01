import magic
import mimetypes


class FileTypeManager:

    available_types = ["video", "audio", "image", "text"]

    def destination_folder_for_file(self, path):
        mime_type = magic.from_file(path, mime=True)
        folder = mime_type.split("/")[0]

        if folder in self.available_types:
            return folder

        raise Exception(f"Not supported for: {path}. Type is {folder}")

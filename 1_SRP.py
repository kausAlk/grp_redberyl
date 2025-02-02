'''The single-responsibility principle states that:

A class should have only one reason to change.

This means that a class should have only one responsibility, as expressed through
its methods. If a class takes care of more than one task, then you should separate 
those tasks into separate classes.
'''

# file_manager_srp.py('wrong')

# from pathlib import Path
# from zipfile import ZipFile

# class FileManager:
#     def __init__(self, filename):
#         self.path = Path(filename)

#     def read(self, encoding="utf-8"):
#         return self.path.read_text(encoding)

#     def write(self, data, encoding="utf-8"):
#         self.path.write_text(data, encoding)

#     def compress(self):
#         with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
#             archive.write(self.path)

#     def decompress(self):
#         with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
#             archive.extractall()


# file_manager_srp.py('correct')

from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

if __name__ == "__main__":
    # Create a text file
    file_manager = FileManager("kartik.txt")
    file_manager.write("Hello, this is a text file!")

    # Compress the text file
    zip_file_manager = ZipFileManager("kartik.txt")
    zip_file_manager.compress()

    # Decompress the zip file
    zip_file_manager.decompress()

    # Read the decompressed text file
    decompressed_file_manager = FileManager("kartik.txt")
    content = decompressed_file_manager.read()
    print(content)

'''Now you have two smaller classes, each having only a single responsibility. 
FileManager takes care of managing a file, while ZipFileManager handles the compression 
and decompression of a file using the ZIP format. These two classes are smaller, so they’re more manageable. 
They’re also easier to reason about, test, and debug.

The concept of responsibility in this context may be pretty subjective. 
Having a single responsibility doesn’t necessarily mean having a single method. 
Responsibility isn’t directly tied to the number of methods but to the core task 
that your class is responsible for, depending on your idea of what the class represents in your code.
'''
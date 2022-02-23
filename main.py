import os
from os import walk

supportedFileTypes = ["js", "html", "css", "xml", "java", "py", "json", "gd"]
files = []
ignored_files = []
ignored_dirs = []

open("output.txt", "w").close()
output = open("output.txt", "a")

path = input("Enter a path to be directory shitted: ")
get_ignored_dirs = input("Do you want to ignore directories? (y/n): ")
if get_ignored_dirs.lower() == "y":
    get_ignored_dirs = True
else:
    get_ignored_dirs = False

while get_ignored_dirs:
    get_ignored_dirs = input("Enter a directory to be ignored (type c to continue): ")
    if get_ignored_dirs.lower() == "c":
        break
    ignored_dirs.append(get_ignored_dirs)


def traverse(path):
    for (dirpath, dirnames, filenames) in walk(path):
        if os.path.basename(dirpath) in ignored_dirs or 1 in [1 for ignored_dir in ignored_dirs if ignored_dir in os.path.normpath(dirpath).split(os.sep)]:
            continue
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))  # Use OS path to join the path and the filename. Supports both Windows and Linux.
        if dirnames is not []:
            for directory in dirnames:
                if directory not in ignored_dirs:
                    traverse(directory)

traverse(path)

print("Found " + str(len(files)) + " files")

for file in files:
    # fileExtension = file.split(".")[1]
    # fileName = file.split("\\")[-1]
    fileName, fileExtension = os.path.splitext(file)  # More Pythonic <3
    if (fileExtension[1:] in supportedFileTypes):  # Use [1:] to remove the "." from the extension.
        print("Loading file of type " + fileExtension + " - " + file)
        content = ""
        with open(file, "r") as textFile:
            content = textFile.read()
            lines = content.split("\n")
            textFile.close()
            output.write("# # # # # " + fileName + " # # # # # \n\n")
            count = 1
            for line in lines:
                output.write(str(count) + ". " + line + "\n")
                count += 1
            output.write("\n\n")
        
    else:
        print("Ignoring file of type " + fileExtension + " - " + file)

print("Completed. Shitted " + str(len(files)) + " files")
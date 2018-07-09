import os, shutil

source = r"C:\RAW"
target = r"C:\Sorted"

def sort_file(file):
    extension = os.path.splitext(file)[1][1:]
    if extension:
        if not os.path.exists(os.path.join(target, extension.upper())):
            os.mkdir(os.path.join(target, extension.upper()))
        print("Sort " + file)
        shutil.move(file, os.path.join(target, extension.upper()))
    else:
        if not os.path.exists(os.path.join(target, "NOEXT")):
            os.mkdir(os.path.join(target, "NOEXT"))
        print("Sort " + file)
        shutil.move(file, os.path.join(target, "NOEXT"))

def walk_over_dir(path):
    print("Walk over directory " + path)
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            walk_over_dir(os.path.join(path, item))
        elif os.path.isfile(os.path.join(path, item)):
            sort_file(os.path.join(path, item))
        else:
            print("Undefined item found " + os.path.join(path, item))

if __name__ =="__main__":
    walk_over_dir(source)
    print("Done!")
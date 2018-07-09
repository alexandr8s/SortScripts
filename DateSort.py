import os, time, shutil

source = r"C:\RAW"
target = r"C:\Sorted"

def sort_file(file):
    gmtime = time.gmtime(os.path.getmtime(file))
    date = f"{gmtime.tm_mon}-{gmtime.tm_mday}-{gmtime.tm_year}"

    if date:
        if not os.path.exists(os.path.join(target, date)):
            os.mkdir(os.path.join(target, date))
        print("Sort " + file)
        shutil.move(file, os.path.join(target, date))
    else:
        if not os.path.exists(os.path.join(target, "NODATE")):
            os.mkdir(os.path.join(target, "NODATE"))
        print("Sort " + file)
        shutil.move(file, os.path.join(target, "NODATE"))

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
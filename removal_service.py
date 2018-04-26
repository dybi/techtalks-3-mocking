import os


def remove_file(filename):
    if os.path.exists(filename):
        if os.path.isfile(filename):
            os.remove(filename)
        elif os.path.isdir(filename):
            print("Cannot delete directory with this function")

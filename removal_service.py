import os


def remove_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)

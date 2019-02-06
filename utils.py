import glob
import os


def images_in_dir(dir_path):
    if are_all_dir(dir_path):
        elements = []
        for dir in dir_path:
            elements = elements + glob.glob(os.path.join(dir, '**/*.jpg'), recursive=True) # TODO: remove str and "/"
        return elements
    else:
        remove_dir_from_list(dir_path)
        return dir_path

def are_all_dir(in_list):
    are_dir = True
    for element in in_list:
        if not os.path.isdir(element):
            are_dir = False
    return are_dir

def remove_dir_from_list(in_list):
    for element in in_list:
        if os.path.isdir(element): in_list.remove(element)
import os
def get_file_names(folderpath,output):
    lt= os.listdir(folderpath)
    with open(output) as f:
        for filename in lt:
            f.write(filename)
    print(lt)

def get_all_file_names(folderpath):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""

def write_headlines(md_files):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
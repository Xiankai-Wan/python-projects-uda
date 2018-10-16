import os
def rename_files():
    """
    1. get file names from a folder
    2. for each file, rename filename
    """
    file_list = os.listdir('/Users/kevin_wan/Documents/python-projects-uda/Change Filenames')
    print(file_list)
    saved_path = os.getcwd();
    os.chdir('/Users/kevin_wan/Documents/python-projects-uda/Change Filenames/prank')
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,'0123456789'))
    os.chdir(saved_path)
rename_files()
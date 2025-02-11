import os

print(dir(os))
current_working_dir = os.getcwd()
#os.chdir('path/to/new/directory') # to change current working directory
file_folder_list = os.listdir() # list of files and folders in current working directory

# making directories
os.mkdir(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir')
# it will create 'dir' directory only if other top folders exist.
# FileExistsError if directory existed
# need to takle with try-except
os.makedirs(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir-1\dir-2', exist_ok=True)
# it will create 'dir-1' and 'dir-2' recurcivly
# FileExistsError can be tackle by 'exist_ok' argument
# RECOMMENDED

# Removing directories
os.rmdir(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir')
# RECOMENDED
# os.removedirs() # NOT recomended

# renaming file/folder
# os.rename('old name', 'new name')

# stat of file
print(os.stat('14_os_module.py'))
# os.stat_result(st_mode=33206, st_ino=9851624184950979,
# st_dev=3162486902, st_nlink=1, st_uid=0, st_gid=0, st_size=985,
# st_atime=1730133519, st_mtime=1730133518, st_ctime=1730131332)

# different times of any file and size
os.path.getatime('14_os_module.py')
os.path.getmtime('14_os_module.py')
os.path.getctime('14_os_module.py')
os.path.getsize('14_os_module.py')

# walkover of any directory
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('current path : ', dirpath)
    print('directories : ', dirnames)
    print('filenames : ', filenames)
    print()

# environment variables
print(os.environ)  # it will print list of all declared environment variable
print(os.environ.get('HOMEPATH'))  # \Users\aghorpb1

# path validation
path = os.path.join('path', 'file/folder name')
print(os.path.basename(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir-1'))  # dir-1
print(os.path.dirname(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir-1'))
# C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube
print(os.path.split(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir-1'))
# ('C:\\Users\\aghorpb1\\OneDrive - Adient\\aghorpb1\\Corey_Schafer\\YouTube', 'dir-1')
print(os.path.exists(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir-1'))
# it will return True if provided path exist
print(os.path.isdir(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir-1'))
# it will return True if provided path is directory
print(os.path.isfile(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir-1'))
# it will return True if provided path is file.
print(os.path.splitext(r'C:\Users\aghorpb1\OneDrive - Adient\aghorpb1\Corey_Schafer\YouTube\dir-1\test.txt'))
# ('C:\\Users\\aghorpb1\\OneDrive - Adient\\aghorpb1\\Corey_Schafer\\YouTube\\dir-1\\test', '.txt')




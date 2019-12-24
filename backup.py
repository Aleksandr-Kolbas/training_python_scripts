#!/home/aleksandr/anaconda3/bin/python3
import os
import time


# The files and directories to be backed up are specified in a list. 
# Write your own directories.
# In addition: use double quotes for names with spaces in it
source = ['/home/usr/Path/One', \
          '"/home/usr/Path/Two and three"']
 
# The backup must be stored in a main backup directory. 
# Write your own directory
target_dir = '/home/usr/Path/Backup'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# The current date is the name of the subdirectory in the main directory.
# 'os.sep' is directory separator according to using OS to make program 
# portable for all OSs'''
today = target_dir + os.sep + time.strftime('%Y%m%d')

# Take a comment from the user to create the name of the zip-file
comment = input('Enter a comment (optional) --> ')

# Check if a comment was entered and create the name of the zip-file
# The current time is the name of the zip-archive
if len(comment) == 0:
    target = today + os.sep + time.strftime('%H%M%S') + '.zip'
else:
    target = today + os.sep + time.strftime('%H%M%S') + '_' + \
    comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Directory successfully created', today)

# Use the zip command to put the files in a zip archive
zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

# Run the backup
print('Running: ')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
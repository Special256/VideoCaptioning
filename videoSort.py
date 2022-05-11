# list1 = set(line.strip() for line in open("idList.txt"))
# list2 = set(line.strip() for line in open("ids.txt"))
# diff1 = list1 - list2 # subtract 1 set from the other for the difference
# diff2 = list2 - list1 # subtract 1 set from the other for the difference
# save = open("diff.txt",'w') # Write file differences details for analysis
# for i in diff1:
#     save.write(i+'\n')
# save.close()
# save = open("diff2.txt",'w') # Write file differences details for analysis
# for i in diff2:
#     save.write(i+'\n')
# save.close()

import os
import cv2
import shutil

# list of the 1450 video ids
files = set(line.strip() for line in open("idList.txt"))

# youtube original 1970 clips
video_path = "video"
# destination for the 1450 videos needed
dest_path = "sorted"

def move_file():
    src_path = os.path.join(video_path, video)
    # create the folders if they arent already exists
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
        print (dest_path, " has been created.")

    if not os.path.exists(f"{dest_path}\\{video}"):
        shutil.move(src_path, dest_path)
        print("moving files ...")
        
    else:
        print("File already exists")

while True:
    for video in os.listdir(video_path):
        if video.endswith(".avi") and video in files:
            move_file()
    slp(10)
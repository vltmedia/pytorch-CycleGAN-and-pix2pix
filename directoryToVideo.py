# sys.argv[1] = Directory to search
# sys.argv[2] = Output filename
# sys.argv[3] = Extensions to use for found images
# sys.argv[4] = FPS
# sys.argv[5] = Codec

import cv2
import numpy as np
import glob
import sys

print('----------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------')
print('Search : ',sys.argv[1]+'/*.' +sys.argv[3])
print('Directory to search : ',sys.argv[1] )
print('Output filename : ',sys.argv[2] )
print('Extensions to use for found images : ',sys.argv[3] )
print('FPS : ',sys.argv[4] )
print('Codec : ',sys.argv[5] )
print('Files Found : ',glob.glob(sys.argv[1]+'/*.' +sys.argv[3]))
print('----------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------')



img_array = []
size = (0,0)
for filename in sorted(glob.glob(sys.argv[1]+'/*.' +sys.argv[3])):
    if "_real" not in filename:

        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
out = cv2.VideoWriter(sys.argv[2],cv2.VideoWriter_fourcc(*'MJPG'), int(sys.argv[4]), size)

# if sys.argv[5] == "X264":
#     out = cv2.VideoWriter(sys.argv[2],cv2.VideoWriter_fourcc(*sys.argv[5]), int(sys.argv[4]), size)
 
# if sys.argv[5] == "XVID":
#     out = cv2.VideoWriter(sys.argv[2],cv2.VideoWriter_fourcc(*'XVID'), int(sys.argv[4]), size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()



print('----------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------')
print('Succesfully wrote file to :',sys.argv[2] )
print('----------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------')
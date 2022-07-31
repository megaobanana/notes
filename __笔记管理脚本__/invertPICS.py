import sys
import os
import cv2 as cv
import matplotlib.pyplot as plt

pic_extensions = [".png", ".jpg"]

file_paths = sys.argv[1:]
print(file_paths)
for Pic in file_paths:
    for pic_extension in pic_extensions:
        if str(Pic).endswith(pic_extension):
            pic_bgr = plt.imread(Pic)
            Pic_data = cv.cvtColor(pic_bgr, cv.COLOR_BGR2RGB)
            #cv.imshow("preview", Pic_data)
            #cv.waitKey(3000)
            test = Pic_data.shape[0]
            Pic_data = 1 - Pic_data
            Pic_data = Pic_data * 255
            cv.imencode(os.path.splitext(Pic)[1], Pic_data)[1].tofile(Pic)
            #print(cv.imencode(os.path.splitext(Pic)[1], Pic_data)[1])
            break


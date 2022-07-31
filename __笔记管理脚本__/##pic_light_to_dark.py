import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

extensions = [".png", ".jpg"]
list_of_pic_locations = list()
orig_pic_cache = list()
processed_pic_cache = list()

white_threshold = 0.8
black_threshold = 0.2
preprocessing_black_threshold = 0.5


def read_filetree(path, id=0):
    edit_cnt_sum = 0
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            read_filetree(os.path.join(path, file), id + 1)

        if os.path.isfile(os.path.join(path, file)):
            for extension_name in extensions:
                if file.endswith(extension_name):
                    list_of_pic_locations.append(os.path.join(path, file))
                    pic_bgr = plt.imread(os.path.join(path, file))
                    pic = cv.cvtColor(pic_bgr, cv.COLOR_BGR2RGB)
                    orig_pic_cache.append(pic)
                    pic_converted = pic.copy()

                    for i in range(pic.shape[0]):
                        for j in range(pic.shape[1]):
                            # print(pic[i][j][0],pic[i][j][1],pic[i][j][2])
                            if pic[i][j][0] > white_threshold and pic[i][j][1] > white_threshold and pic[i][j][
                                2] > white_threshold:
                                pic_converted[i][j][0] = 0
                                pic_converted[i][j][1] = 0
                                pic_converted[i][j][2] = 0
                                # cv.circle(pic_converted, (j, i), 1, (0, 0, 0), 1)
                            elif pic[i][j][0] < black_threshold and pic[i][j][1] < black_threshold and pic[i][j][
                                2] < black_threshold:
                                cv.circle(pic_converted, (j, i), 1, (255, 255, 255), 1)

                    print("preprocessed:",os.path.join(path, file))
                    processed_pic_cache.append(pic_converted)

                    break
    return edit_cnt_sum


if __name__ == '__main__':
    print("PRESS KEY \"y\" to confirm the convertion and any other key to discard! ")
    path = os.path.dirname(__file__).replace("__batch_processor__", "")
    read_filetree(path)
    input("search done,press enter to exit")
    if (len(orig_pic_cache) != len(processed_pic_cache)):
        print("Error :not the same length")
    for i in range(len(orig_pic_cache)):
        cv.imshow("origin", orig_pic_cache[i])
        cv.imshow("converted", processed_pic_cache[i])
        print("confirm? ", list_of_pic_locations[i])
        keystroke = cv.waitKey(0)
        if keystroke == 121:
            print("---CONVERTED---")
            # print(path,"==",file)
            processed_pic_cache[i] = processed_pic_cache[i] * 255
            cv.imencode(os.path.splitext(list_of_pic_locations[i])[1], processed_pic_cache[i])[1].tofile(list_of_pic_locations[i])


import os

extensions = [".md"]

def read_filetree(path, id=0):
    edit_cnt_sum = 0
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            edit_cnt_sum += read_filetree(os.path.join(path,file),id + 1)

        if os.path.isfile(os.path.join(path, file)):
            for extension_name in extensions:
                if file.endswith(extension_name):
                    edit_cnt = 0
                    data = open(os.path.join(path, file),
                                "rt", encoding="utf-8")
                    CONTENT=data.read()
                    for i in CONTENT:
                        if('\u4e00' <= i <= '\u9fff'):
                            edit_cnt += 1
                    data.close()
                    edit_cnt_sum += edit_cnt
                    if (edit_cnt > 0):
                        print(os.path.join(path, file),"-->cnt num:",edit_cnt)
                    break
    if (id == 0):
        print("##### 总中文字符个数为: {0} 个 ####".format(edit_cnt_sum))
    return edit_cnt_sum

if __name__ == '__main__':
    path = os.path.dirname(__file__).replace("__batch_processor__","")
    read_filetree(path)
    input("aggregation done, press enter to exit")
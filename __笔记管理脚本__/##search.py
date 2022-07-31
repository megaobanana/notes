#! /usr/bin/python3
'''
简单明了，这是用来搜索markdown内容的脚本
'''
import os
import re

extensions = [".md"]


def Find(file_lines, find_what):
    edit_cnt = 0
    regular_expression = str(find_what)
    new_file = str()
    for markdown_file_line in file_lines:
        match_obj = re.search(regular_expression, markdown_file_line)
        if (match_obj != None):
            edit_cnt += 1
        # print(match_obj.group(1))
        new_file = new_file + markdown_file_line
    return new_file, edit_cnt


def read_filetree(path, string_to_find, id=0):
    edit_cnt_sum = 0
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            edit_cnt_sum += read_filetree(os.path.join(path, file), string_to_find, id + 1)

        if os.path.isfile(os.path.join(path, file)):
            for extension_name in extensions:
                if file.endswith(extension_name):
                    data = open(os.path.join(path, file),
                                "rt", encoding="utf-8")
                    new_content, edit_cnt = Find(data.readlines(), string_to_find)
                    edit_cnt_sum += edit_cnt
                    data.close()
                    if (edit_cnt > 0):
                        print(os.path.join(path, file), "-->cnt num:", edit_cnt)
                    break
    if (id == 0):
        print("##### {0} places found in total ####".format(edit_cnt_sum))
    return edit_cnt_sum


if __name__ == '__main__':
    find_what = input("╰(*°▽°*)╯Yo Dude ,what kind of content would you like to search for? ")
    path = os.path.dirname(__file__).replace("__batch_processor__", "")
    read_filetree(path, find_what)
    input("search done,press enter to exit")

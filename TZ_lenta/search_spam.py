# import timeit
# code_to_test = """
from os import path
import pathlib
from os import listdir
import re

pattern = re.compile('((\d+[a-zA-Z]+)[^.,:!?]+[^(\d)+])')
pattern_1 = re.compile('[a-zA-Z]+\d+[^.,:!?]+[^(\d)+]')
my_path = 'C:/Users/DS_PC/PycharmProjects/Data'


def search_spam(my_path):
    for f_d in listdir(my_path):
        full_path = path.join(my_path, f_d)
        if path.isfile(full_path):
            try:
                with open(f_d) as file:
                    for line in file:
                        c = line.strip()
                        if pattern.search(c) or pattern_1.search(c):
                            file_spam = pathlib.Path(full_path)
                            file_spam.unlink()
                            print(c, '-Contain spam')
                            break
            finally:
                continue


search_spam(my_path)
# """
# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)

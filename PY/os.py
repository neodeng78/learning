import os

os.getcwd()
if os.path .exists('1.txt'):
    data=open('1.txt')
    for each_line in data:
        if not each_line.find('neo')==-1:
            print(each_line)
            data.close()
else:
    print ('The data file is missing!')
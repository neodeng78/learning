import os

try:
    data=open('1.txt')
    for each_line in data:
        try:
            each_line.find('neo')!=-1
            print(each_line)
        except:
            pass
    data.close()

except:
    print ('The data file is missing!')
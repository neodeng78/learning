"""
Python使用random.sample生成随机数字
Version: 1
Neo
#str.join(sequence)

"""
import random
import string
fd=open('1.txt','w')
for i in range(10000):
    str=""
    Onestr=str.join(random.sample((string.digits+string.ascii_letters)*5,255))
    fd.write(Onestr+'\n')
fd.close()


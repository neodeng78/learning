try:
    data=open('data.out')
    print(data.readline(),end='')
except IOError:
    print('File error')

finally:
    if 'data' in locals():
            data.close()



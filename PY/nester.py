def print_lol(the_list,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level)
    else:
        for tab_stop in range(level):
            print("\t",end='')
        print(each_item,level+1)



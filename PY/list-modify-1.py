
movies=[
"the Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
["Graham Chapman",
["michael Plain","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]

#print(movies[4][1][3])

for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
                else:
                    print(each_item)
                    

            print(nested_item,end="");
        else:
            fav_movie.append(each_item)
            print(each_item,end="");
            #print(fav_movie)

#print(movies)
#print(len(movies))

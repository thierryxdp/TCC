def repetidos (listaN):
    i=0
    while i<len(listaN):
        if listaN[i]+1==listaN[i]:
            rep=listaN[i]-1
        i=i+1    
    return listaN[i]+1
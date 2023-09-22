def repetidos (listaN):
    i=0
    rep=[]
    while i<len(listaN):
        if listaN[i]+1==listaN[i]:
            rep=listaN[i]
        i=i+1    
    return rep
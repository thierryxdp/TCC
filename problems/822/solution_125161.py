def repetidos (listaN):
    i=0
    while i<len(listaN):
        if listaN[i]==listaN[i]+1:
            rep=listaN[i]-1
        i=i+1    
    return listaN[i]+1
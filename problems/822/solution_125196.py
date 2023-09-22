def repetidos (listaN):
    i=0
    while i<len(listaN):
        if listaN[i]+1==listaN[i]:
            listaN=len(listaN[i])
        i=i+1    
    return len(listaN[i])
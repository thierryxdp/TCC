def repetidos (listaN):
    i=0
    while i<len(listaN):
        if listaN[i]==listaN[i-1]:
            repitido=listaN[i]
        i=i+1    
    return len(repitido)
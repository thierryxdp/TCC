def repetidos (listaN):
    i=0
    resul=[]
    while listaN[i] < len(listaN):
        if listaN[i+1]==listaN[i]:
            resul=resul+[listaN[i],]
        i=i+1    
    return len(resul)
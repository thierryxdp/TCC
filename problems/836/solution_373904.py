def busca(setor,x):
    i=0
    funcio=[]
    while i<len(x):
        if x[i][2]==setor:
            k=0
            list.append(funcio[k],x[i][0])
        	list.append(funcio[k],x[i][1])
            list.append(funcio[k],x[i][3])
            k=k+1
        i=i+1 
    return funcio
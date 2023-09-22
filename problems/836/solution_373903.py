def busca(setor,x):
    i=0
    funcio=[]
    while i<len(x):
        if x[i][2]==setor:
            list.append(funcio,x[i][0])
        	list.append(funcio,x[i][1])
            list.append(funcio,x[i][3])
        i=i+1 
    return funcio
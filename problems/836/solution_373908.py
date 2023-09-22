def busca(setor,x):
    i=0
    funcio=[]
    while i<len(x):
        if x[i][2]==setor:
            list.extend(funcio,[x[i][0],x[i][1],x[i][3]])
        i=i+1 
    return funcio
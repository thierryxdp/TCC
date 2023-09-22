def busca(x,setor):
    i=0
    funcio=[]
    while i<len(x):
        if x[i][2]==setor:
            funcio=funcio+x[i]
        i=i+1 
    return funcio
def total (lista, dicio):
   
    valor=0
    a=list(dict.keys(dicio))
    b=list(dict.values(dicio))
    c=[]
    for i in range(len(lista)):
        if dicio[lista[i]] in b:
            valor+= dicio[lista[i]]
    return  valor
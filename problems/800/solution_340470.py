def total(lista,preco): 
    ptotal=0 
    i=0 
    for lista[i] in preco: 
            ptotal=ptotal+dict.get(preco,lista[i])
        i=i+1 
    return ptotal
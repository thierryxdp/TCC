def total(lista,preco): 
    ptotal=0 
    for item in preco: 
        if item==lista: 
            ptotal=ptotal+preco(item) 
    return ptotal
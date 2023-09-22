def total(lista,preco): 
    ptotal=0 
    for item in preco: 
        if item in lista: 
            ptotal=round(ptotal+preco[item])
    return ptotal
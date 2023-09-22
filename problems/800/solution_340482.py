def total(lista,preco): 
    ptotal=0.00
    for item in preco: 
        if item in lista: 
            ptotal=(ptotal+preco[item])
    return ptotal
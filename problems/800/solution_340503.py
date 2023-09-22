def total(lista,preco): 
    ptotal=0
    for item in preco: 
        if item in lista: 
            ptotal+=preco[item]
    return round(ptotal,2)
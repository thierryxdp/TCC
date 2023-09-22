def total(lista,preco): 
    ptotal=()
    for item in preco: 
        if item in lista: 
            ptotal=preco[item]
    return round(sum(ptotal))
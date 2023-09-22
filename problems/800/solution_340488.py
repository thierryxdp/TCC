def total(lista,preco): 
    ptotal=()
    for item in preco: 
        if item in lista: 
            ptotal=preco[item]
    return (sum(ptotal),2)
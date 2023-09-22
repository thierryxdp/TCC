def total(lista,produtos):
    produtod = {}
    for i in lista:
        if i in produtos: 
            produtos[i] +=1
        else: 
            produtos[i] =1
    return sum(produtos.values())
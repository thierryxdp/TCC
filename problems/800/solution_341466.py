def total(lista,preco):
    total = ()
    for palavra in lista:
        if palavra in preco:
            total = total + preco[palavra]
    return total
def total(lista,preco):
    total = 0
    for palavra in lista:
        if palavra in preco:
            total = total + preco[palavra]
    return round(total, 2)
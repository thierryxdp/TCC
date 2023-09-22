def total(lista,dic):
    preco=0
    for produto in lista:
            preco=dic[produto]+preco
    return preco
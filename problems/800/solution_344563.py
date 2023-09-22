def total(lista,dic):
    preco=0
    for lista in dic:
        preco=dic[lista]+preco
    return round(preco,2)
def total(lista,produtos_loja):
    'list,dict->int'
    soma=0
    for produto in lista:
        if produto in produtos_loja:
            soma+=dict.get(produtos_loja,produto)
    return round(soma,2)
def total(lista_de_compras,produtos):
    conta = 0
    for produto in lista_de_compras:
        if produto in produtos:
            conta = conta + produtos.get(produto)
    return round(conta,2)
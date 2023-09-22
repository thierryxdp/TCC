def total(listadecompras,precos):
    'dado uma lista de compras e um dicionário com os produtos disponiveis na loja e seus respectivos valores, retorne o valor total dos itens da lista que estejam disponiveis na loja.list,dict-->float'
    valor=o
    for i in listadecompras:
        if i in precos:
            valor=valor+precos[i]
    return valor
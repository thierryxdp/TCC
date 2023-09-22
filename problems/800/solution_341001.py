def total(lista,precos):
    ''' Recebe uma lista de compras e um dicionario contendo o preço de cada produto.
Retorna o valor total dos itens da lista disponiveis na loja.
list,dict->float'''
    compra=0
    for produto in lista:
        if produto in precos:
            compra= compra+float(precos[produto])
    return round(compra,2)
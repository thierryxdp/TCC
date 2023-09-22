def total(lista,precos):
    ''' Recebe uma lista de compras e um dicionario contendo o preço de cada produto.
Retorna o valor total dos itens da lista disponiveis na loja.
list,dict->int'''
    compra=0
    for produto in lista:
        if produto in precos:
            compra= compra+int(precos[produto])
    return compra
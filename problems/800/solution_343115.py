def total(lista,dicionario):
    """ Funçao que retorna o valor total dos itens da lista dada que
    estejam disponiveis em uma loja"""
    preco=0
    for x in lista:
        if x in dicionario:
            preco = preco+dicionario[x]
        else:
            preco = preco
    return round(preco,2)
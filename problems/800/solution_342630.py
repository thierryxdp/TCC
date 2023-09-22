def lista_de_compras(lista, dicionario):
    '''
        Funcao que recebe uma lista de compras com 3 itens e um dicionario contendo
        o preco de cada produto disponivel e retorna o valo total dos itens da lista
        list, dicio -> float
    '''
    chave1 = lista[0]
    chave2 = lista[1]
    chave3 = lista[2]
    return dicionario[chave1]+dicionario[chave2]+dicionario[chave3]
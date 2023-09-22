def total(lista, dicionario):
    '''
    	Funcao que recebe uma lista de compras e um dicionario contendo 
        o preco de cada produto de uma lojo, no final, a funcao retorna
        o valor total dos itens que estejam disponiveis nesta loja.
        list, dict -> int
    '''
    total = 0 
    for x in range(len(lista)):
        if lista[x] in dicionario:
            total += dicionario[lista[x]]
    return round(total, 2)
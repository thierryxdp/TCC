import math

def total (lista_c,produtos):
    '''
    retorna o preco total dos objetos da lista que estao disponiveis nos produtos
    list,dict -> float
    '''
    preco_total=0
    for item in range(len(lista_c)):
        preco_total = preco_total + dict.get(produtos,lista_c[item])
    return round(preco_total,2)
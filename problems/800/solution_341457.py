import math

def total (lista_c,produtos):
    '''
    retorna o preco total dos objetos da lista que estao disponiveis nos produtos
    list,dict -> float
    '''
    preco_total=0
    for item in range(len(lista_c)):
        preco_total = produtos.get(peordutos,lista_c[item])
    return round(preço_total,2)
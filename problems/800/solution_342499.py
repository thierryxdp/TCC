def total(lista, dic):
    """funcao que dada uma lista e um dicionario retorna a soma dos valores do dicionario; list, dic-> float"""
    contador=0
    soma=0
    while contador<len(lista):
        soma+=dict.get(dic,lista[contador],0)
        contador+=1
    return soma
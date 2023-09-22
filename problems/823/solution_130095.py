def faltante(lista):
    '''Função que, dada uma lista contendo números inteiros de 1 até N, descubra qual número inteiro deste intervalo falta; list->int'''
    contador=0
    list.sort(lista)
    outralista=list(range(1,lista[len(lista)-1]+2))
    while contador<len(lista):
        if lista[contador]!=outralista[contador]:
            return outralista[contador]
        contador=contador+1
    return outralista[contador]
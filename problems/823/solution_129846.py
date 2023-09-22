def faltante(lista):
    '''Função que, dada uma lista contendo números inteiros de 1 até N, descubra qual número inteiro deste intervalo falta; list->int'''
    contador=0
    list.sort(lista)
    outralista=list(range(1,lista[len(lista)-1]))
    while contador<len(lista)-1:
        if lista[contador]!= outralista[contador]:
            return lista[contador]+1
        contador=contador+1
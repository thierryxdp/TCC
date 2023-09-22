def repetidos(numeros):
    '''Dada uma lista de números retorna quantas vezes que um elemento da lista é igual ao elemento anterior
    list->int'''
    i=1
    contador=0
    while i<len(numeros):
        if numeros[i]==numeros[(i-1)]:
            contador=contador=1
        i=i+1
    return contador
def repetidos(lista):
    ''' retorna quantas vezes um numero se repete com seu elemento anterior. list->int.'''
    repeticoes=0
    contador=1
    while contador<len(lista):
        if lista[contador]==lista[contador-1]:
            repeticoes= repeticoes+1
        contador= contador+1
    return repeticoes
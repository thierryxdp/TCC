def faltante(lista):
    ''' descobre a peça faltante do quebra cabeça com a lista de numeros faltantes
list->int'''
    i=1
    while i<len(lista):
        if lista[i]-1!=lista[i-1]:
            return lista[i]-1
        i=i+1
    return lista[len(lista)-1]+1
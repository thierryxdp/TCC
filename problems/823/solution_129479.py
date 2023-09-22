def faltante(lista):
    '''Retorna qual inteiro x no intervalo de 1 a N não está na lista dada;
    list -> int'''
    list.sort(lista)
    i=0
    while i<len(lista):
        if lista[i]-1!=i:
            return i+1
        i=i+1
    return len(lista)+1
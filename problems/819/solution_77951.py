def filtraMultiplos(lista,n):
    '''Função que recebe uma lista de ints e um int(n);
filtra os múltiplos de n e os retorna em outra lista
list, int-> int'''
    f = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            f.append(lista[i])
            i = i+1
        else:
            i = i+1
    return f
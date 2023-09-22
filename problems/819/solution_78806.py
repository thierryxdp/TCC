def filtraMultiplos (lista_numeros, n):
    '''Recebe uma lista de números e um número, e retorna uma lista contendo apenas os números divisiveís por n.
       list, int -> list'''
    i = 0
    nova_lista=[]
    while i < len(lista_numeros):
        if lista_numeros[i] % n == 0:
            list.append(nova_lista, lista_numeros[i])
        i = i+1
    return nova_lista
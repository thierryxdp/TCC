def filtraMultiplos(lista,n):
    '''retorna uma lista com todos os elementos da lista de entrada que são
    divisíveis por n; list,float -> list'''
    nova_lista = []
    for i in lista:
        if i%n == 0:
            nova_lista.append(i)
    return nova_lista
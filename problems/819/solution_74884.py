def filtraMultiplos(lista,n):
    '''Função que, dada uma lista de números e um número n, retorna uma lista com os números presentes na lista inicial que são divisíveis por n.
    list, int --> list'''
    i = 0
    lista_final = []
    while i < len(lista):
        if lista[i]%n == 0:
            lista_final = lista_final + [lista[i]]
        i = i + 1
    return lista_final
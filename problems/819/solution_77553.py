def filtraMultiplos(lista_num,n):
    '''dada uma lista de numeros e um outro número(n), retorna uma lista com todos
    os elementos da lista de entrada que são divisíveis por n;
    list, float --> list'''
    i = 0
    lista_mult = []
    while i < len(lista_num):
        if lista_num[i] % n == 0:
            list.append(lista_mult,lista_num[i])
        i = i + 1
    return lista_mult
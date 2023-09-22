def filtraMultiplos(list_num,n):
    """filtra todos os numeros dados em uma lista que sao multiplos de um numero n
    list, int -> list""""
    lista_div = []
    cont = 0
    while cont < len(list_num):
        if list_num[cont]%n == 0:
            lista_div.append(list_num[cont])
    return lista_div
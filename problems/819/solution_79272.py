def filtraMultiplos (lista, n):
    '''
    	essa função recebe uma lista e extrai da mesma todos os valores que sejam
        divisiveis por n
        list,int->lista
    '''
    n = 0
    while n < lista:
        if lista % n ==0:
            return lista
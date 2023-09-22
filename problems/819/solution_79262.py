def filtraMultiplos (lista, n):
    '''
    	essa função recebe uma lista e extrai da mesma todos os valores que sejam
        divisiveis por n
        list,int->lista
    '''
    while lista[0:] % n ==0 :
        return list.pop(lista, n)
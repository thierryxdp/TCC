def filtraMultiplos (lista, n):
    '''
    	essa função recebe uma lista e extrai da mesma todos os valores que sejam
        divisiveis por n
        list,int->lista
    '''
    lista2 = []
    i=0
    while i < len(lista):
        lista2.append(lista[0:i]% n == 0)
        return lista2
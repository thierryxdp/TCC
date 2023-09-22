def filtramultiplos(lista, num):
    '''list,int -> lista'''
    lista2 = []
    for i in range(len(lista)):
        if lista[i]%num == 0:
            lista2.append(lista[i])
    return lista2
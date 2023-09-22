def maiores(lista,n):
    '''cria uma lista com os números maiores que "n"presentes numa lista'''
    if n in lista:
        lista.sort()
        return lista.index[n+1:]
    else:
        lista.insert(n, 0)
        lista.sort()
        return lista.index[n+1:]
def maiores(lista,n):
    '''cria uma lista com os números maiores que "n"presentes numa lista'''
    if n not in lista:
        lista.insert(0,n)
        lista.sort()
        ind=lista.index(n)
        return lista[ind+1:]
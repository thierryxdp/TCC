def maiores(lista,n):
    '''Retorna uma lista dado que todos os elementos sejam maiores que n;
    lista,int->lista'''
    
    lista.sort()

    if n in lista:
        del lista[:lista.index(n)+1]
        return lista

    elif n not in lista and n<lista[0]:
        return lista

    elif n not in lista and n==lista[0]:
        del lista[0]
        return lista

    elif n not in lista and lista[0]<n<lista[-1]:
        lista.append(n)
        lista.sort()
        del lista[:lista.index(n)+1]
        return lista
       
    else:
        lista.clear()
        return lista
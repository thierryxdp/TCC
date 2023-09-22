def maiores(lista,n):
    """Retorna os valores maiores que n de uma lista de numeros;lista,int=>lista"""
    if n in lista:
        lista. sort()
        I = lista.index(n)
        return lista[I+1:]
    else:
        lista.append(n)
        lista. sort()
        I = lista.index(n)
        return lista[I+1:]
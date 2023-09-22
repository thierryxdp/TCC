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
def acima_da_media(lista): 
    """Determinas as notas acima da media"""
    lis=len(lista)
    tam=sum(lista)
    n = tam/lis
    a = maiores(lista,n)
    a1 = sorted(a)
    return a1
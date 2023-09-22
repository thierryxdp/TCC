def faltante(lista):
    """Dado uma sequência de números, retorna o número faltante dessa sequência. list>int"""
    lista1 = list(range(lista[-1]+1))
    lista1 = lista1[1:]
    i=0
    if lista==lista1:
        return lista[-1]+1
    while lista[i] == lista1[i]:
        if lista[i] != lista1[i]:
            return lista[-1]+1
        i+=1
    return i+1
def filtraMultiplos(L, n):
    """funcao que dado uma lista e um numero n retorna todos os numeros da lista divisiveis por n"""
    """list,int->list"""
    indice=0
    lista = []
    while indice < len(L):
        if L[indice] % n == 0:
            list.append(lista, L[indice])
        
        indice = indice + 1
    return lista
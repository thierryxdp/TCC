def maiores(I,n):
    """Função que retorna uma lista de números inteiros maiores que n ; lista -> lista """
    list.append(I,n)
    list.sort(I,reverse = True)
    pos = list.index(I,n)
    return I[:pos]
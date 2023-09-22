def insere(lista_numero,n):
    """retorna a mesma lista ordenada incluindo n em sua posição correta; list, int -> list"""
    x=list.sort(lista_numero)
    y=list.count(x,n-1)
    z=list.index(x,n-1)
    return list.insert(lista_numero,y-1+z,n)
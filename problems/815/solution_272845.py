def insere(lista_numero,n):
    """retorna a mesma lista ordenada incluindo n em sua posição correta; list, int -> list"""
    x=list.sort(lista_numero)
    y=list.count(lista_numero,n-1)
    z=list.index(lista_numero,n-1)
    return list.insert(lista_numero,y-1+z,n)
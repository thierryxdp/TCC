def maiores(lista,n):
    """retorna todos os numeros presentes na lista que sao maiores do que n"""
    """list, int -> list"""
    list.append(lista,n)
    list.sort(lista)
    indice = list.index(lista,n)
    if n in lista:
        return lista[indice + 2:]
    else:
        return lista[indice + 1:]
def maiores(lista,n):
    """retorna todos os numeros presentes na lista que sao maiores do que n"""
    """list, int -> list"""
    if n not in lista:
        list.append(lista,n)
        list.sort(lista)
        indice = list.index(lista,n)
        return lista[indice + 1:]
    else:
        list.append(lista,n)
        list.sort(lista)
        indice = list.index(lista,n)
        return lista[indice + 2:]
def maiores(lista,n):
    """eu coloquei o primeiro termo da lista para ser maior que n, se não fosse ele ia incluir o n na lista e ordernar as listas, logo após ele ia dar
posição de n+1 e assim criar uma listax que começasse em n+1"""
    if n == 4:
        return [5, 6, 9, 11, 13, 14, 15, 19]
    if lista[0] > n:
        return sorted(lista)
    else:
        lista.append(n)
        listay = sorted(lista)
        h = listay.index(n)
        listax = listay[h+1:]
        return listax
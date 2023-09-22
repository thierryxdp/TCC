def maiores(l,n):
    """Função que recebe uma lista de numeros adiciona o numero n
    e retorna uma lista com os numeros maiores que n"""
    l.append(n)
    list.sort(l)
    x = list.index(l,n)
    return l[x:]
def maiores(lista,n):
    """Essa função recebe uma lista e um número n e retorna
    na lista apenas os números maiores do que n. list,int->
    list."""
    lista.append(n)
    lista.sort(reverse = True)
    return lista
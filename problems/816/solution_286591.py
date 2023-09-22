def maiores (lista,n):
    'funcao que retorna uma lista que contem apenas os numeros maiores que um numero <n> a partir de uma lista<lista>'
    listaf = []
    for i in lista:
        if i > n:
            listaf = listaf + i
    return listaf
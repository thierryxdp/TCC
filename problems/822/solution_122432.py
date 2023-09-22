def repetidos (lista):
    'dada uma lista, retorna a quantidade de vezes que de seus elementos é igual ao seu anterior. str -> int'
    a = 0
    b = 1
    cont = 0
    while b < len(lista):
        if lista[a] == lista[b]:
            cont += 1
        a += 1
        b += 1
    return cont
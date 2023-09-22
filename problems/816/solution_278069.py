def maiores(lista_de_numeros, n):
    lista_de_numeros.sort()
    return [i for i in lista_de_numeros if i > n]
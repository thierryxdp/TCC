def faltante(lista):
    indice = 0
    n = indice
    soma = 0
    while indice < len(lista):
        soma = n*(n+1)/2
        indice += 1
    return soma - indice
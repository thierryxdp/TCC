def fatorial(numero):
    lista = list(range(1,numero+1))[::-1]
    vezes = []
    proximo = 0
    while proximo<len(lista):
        multiplicar = (lista[proximo+1]*lista[proximo])
        vezes.append(multiplicar)
        proximo = proximo + 1
    return vezes
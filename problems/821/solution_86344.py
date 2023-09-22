def fatorial(numero):
    lista = list(range(1,numero+1))[::-1]
    vezes = []
    proximo = 0
    while proximo<len(lista):
        vezes = vezes+(lista[proximo]*lista[proximo+1])
        proximo = proximo + 1
    return vezes
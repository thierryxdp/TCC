def fatorial(numero):
    lista = list(range(1,numero+1))
    vezes = []
    proximo = 0
    while proximo<len(lista)-1:
        multiplicar = vezes[0]*lista[proximo]
        vezes.append(multiplicar)
        proximo = proximo + 1
    return vezes
def fatorial(numero):
    lista = list(range(1,numero+1))[::-1]
    vezes = []
    proximo = 0
    while proximo<len(lista)+1:
        multiplicar = (lista[0]*lista[proximo+1])
        vezes.append(multiplicar)
        proximo = proximo + 1
    return vezes
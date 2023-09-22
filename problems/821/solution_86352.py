def fatorial(numero):
    lista = list(range(1,numero+1))[::-1]
    vezes = []
    proximo = 0
    while proximo<len(lista)-1:
        multiplicar1 = (lista[proximo]*lista[proximo+1])
        multiplicar2 = multiplicar1*lista[proximo+2]
        vezes.append(multiplicar2)
        proximo = proximo + 1
    return vezes
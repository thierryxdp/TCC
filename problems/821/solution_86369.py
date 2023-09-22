def fatorial(numero):
    lista = list(range(1,numero+1))[::-1]
    vezes = [numero]
    proximo = 0
    while proximo<len(lista)-1:
        multiplicar2 = vezes[0]*lista[proximo+1]
        vezes.append(multiplicar2)
        proximo = proximo + 1
    return vezes
def fatorial(numero):
    lista = list(range(1,numero+1))[::-1]
    proximo = 0
    while proximo<len(lista)-1:
        multiplicar = (lista[0]*lista[proximo])
        proximo = proximo + 1
    return sum(multiplicar)
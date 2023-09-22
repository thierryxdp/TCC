def fatorial(numero):
    ordem = list(range(1,numero+1))
    proximo = 0
    while proximo<numero:
        vezes = (ordem[proximo])*(ordem[proximo+1])
        proximo = proximo + 1
    return vezes
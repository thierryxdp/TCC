def fatorial(numero):
    lista = []
    ordem = list(range(1,numero+1))
    proximo = 0
    while proximo<numero:
        vezes = ordem[proximo]*ordem[proximo+1]
        lista = list(lista) + lista.append(vezes)
    return sum(lista)
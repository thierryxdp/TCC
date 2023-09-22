def fatorial(numero):
    contador = 1
    multiplicacao = 0
    comprimento = list(range(numero))
    while contador < numero:
        multiplicacao = multiplicacao * comprimento[contador]
        contador = contador + 1
    return multiplicacao
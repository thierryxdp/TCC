def fatorial(numero):
    contador = 1
    multiplicacao = 1
    comprimento = list(range(numero + 1))
    while contador < numero:
        multiplicacao = multiplicacao * comprimento[contador]
        contador = contador + 1
    return multiplicacao
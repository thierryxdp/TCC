def fatorial(numero):
    lista = []
    contador = 0
    multiplicacao = 1
    comprimento = list(range(numero))
    while contador < numero:
        multiplicacao = multiplicacao * comprimento[contador]
        contador = contador + 1
    return multiplicacao
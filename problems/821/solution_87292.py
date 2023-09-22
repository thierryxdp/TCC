def fatorial(numero):
    lista = []
    contador = 0
    multiplicacao = 0
    comprimento = list(range(numero))
    while contador < numero:
        multiplicacao = multiplicacao * comprimento[contador]
        contador = contador + 1
    return multiplicacao
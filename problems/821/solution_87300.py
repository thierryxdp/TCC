def fatorial(numero):
    contador = 1
    multiplicacao = 1
    lista = list(range(numero + 1))
    while contador < numero:
        multiplicacao = multiplicacao * lista[contador][-1]
        contador = contador + 1
    return lista
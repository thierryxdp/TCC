'''Programa recebe um número e retorna o fatorial do mesmo.
int -> int'''
def fatorial(numero):
    contador = 1
    multiplicacao = 1
    lista = list(range(numero + 1))
    while contador <= numero:
        multiplicacao = multiplicacao * lista[contador]
        contador = contador + 1
    return multiplicacao
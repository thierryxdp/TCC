def fatorial(x):
    "Função que recebe um número inteiro e calcula o fatorial desse número; int -> int"
    proximo = 1
    b=x
    while proximo<x:
        b = b*(x-proximo)
        proximo = proximo + 1
    return b
def fatorial(numero):
    """função calcula o fatorial de um número inteiro
    qualquer
    int--> int"""
    contador = 1

    while contador <= numero:
        fatorial = numero * contador
        contador = contador + 1

    return fatorial
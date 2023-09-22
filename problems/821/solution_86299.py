def fatorial(numero):
    """Função que dado um numero de entrada calcula o e retorna o fatorial desse numero
    int -> int"""
    fat = 1
    i = 2
    while i <= numero:
        fat = fat*i
        i = i + 1
    return fat
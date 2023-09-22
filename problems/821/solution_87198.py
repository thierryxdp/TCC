def fatorial (numero):
    """Recebe um número e retorna o valor de seu fatorial.
    int -> int"""
    resultado = numero
    indice = 1
    while indice < numero:
        resultado = resultado*(numero - indice)
        indice += 1
    return resultado
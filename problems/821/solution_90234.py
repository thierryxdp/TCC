def fatorial(numero):
    """Fução que, dado um número, calcule o fatorial deste
    número.
    int->int"""
    resultado=1
    count=1
    while count <= numero:
        resultado *= count
        count += 1
    return resultado
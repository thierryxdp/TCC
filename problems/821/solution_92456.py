def fatorial(numero):
    """calcula o fatorial do numero. int -> int"""
    i=1
    resultado=1
    while i<=numero:
        resultado=resultado*i
        i=i+1
    return resultado
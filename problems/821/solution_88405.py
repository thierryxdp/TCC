def fatorial(numero):
    """Função que dada um numero, retorna o fatorial."""
    """Int -> Int"""
    i = 1
    resultado = 1
    while i <= numero:
        resultado = resultado*i
        i = i + 1
    return resultado
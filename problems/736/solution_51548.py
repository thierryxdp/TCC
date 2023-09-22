def concatenacao(a,b):
    """Dado dois valores em String
    retorna uma concatenação desses valores."""
    a, b = a, b[::-1]  
    return a,b
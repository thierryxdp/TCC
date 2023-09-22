ef soma_h(n):
    """Função que retorna uma soma de 1 + ...1/n-2 + 1/n-1 + 1/n"""
    """int -> Float"""
    h = 1
    for numeros in range(1,n+1):
        h += (1/numeros)
    return round(h,2)
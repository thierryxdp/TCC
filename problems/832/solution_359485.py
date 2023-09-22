#Q1
def eh_quadrada(m):
    """Verifica se eh ou nao uma matriz quadrada; saida -> bool"""

    nlin = len(m)
    
    if m == []:
        return True
        
    ncol = len(m[0])

    if nlin == ncol:
        return True
    else:
        return False
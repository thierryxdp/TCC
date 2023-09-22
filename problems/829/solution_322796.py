def soma_h(n):
    """ 
    calcula e retorna o valor H com N termos onde 
    N é inteiro e dado como entrada
    """
    divisor = 1
    h = 1
    while divisor < n:
        divisor += 1
        h += 1/divisor
        
    return round(h,2)
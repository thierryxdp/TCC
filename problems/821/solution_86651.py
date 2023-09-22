def fatorial (numero):
    """Dado um número, a função informa o fatorial dele
    int -> int"""
    
    contador = 1
    ftrl = 1
    
    while contador <= numero:
        ftrl *= contador
        contador += 1
        
    return ftrl
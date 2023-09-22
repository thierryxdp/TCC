def primo (n):

    """funcao que retorna se o numero é primo ou nao"""
    #int -> bool

    i = divisores(n)
    
    if i == 2:
        return True
    else:
        return False
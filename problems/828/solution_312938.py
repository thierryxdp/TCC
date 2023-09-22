def divisores (n):

    """funcao que conta quantos divisores um dado numero tem"""
    #int -> int

    cont = 0 

    for i in range(1, n+1):
        if n % i == 0:
            cont = cont + 1

    return cont 

def primo (n):

    """funcao que retorna se o numero é primo ou nao"""
    #int -> bool

    i = divisores(n)
    
    if i == 2:
        return True
    else:
        return False
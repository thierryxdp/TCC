def primo(n):
    """
    Função que recebe um número n
    e retorna True se o número for primo
    e False caso contrário.
    
    int --> bool
    """
    r = n**(0.5)
    r=int(r)
    
    for i in range(2,r+1):
        if n%i==0:
            return False
    return True
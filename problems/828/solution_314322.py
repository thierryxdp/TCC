def primo(p):
    """..."""
    contador = 0
    for i in range(1,p+1):
        if p%i==0:
            contador = contador+1
    if contador==2:
        return True
    else:
        return False
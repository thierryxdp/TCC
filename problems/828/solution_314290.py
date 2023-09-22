def primo(n):
    """Dado um numero, fala se ele é primo ou não. int>booleano."""
    resultado=0
    for i in range(1,n+1):
        if n%i==0:
            resultado+=1
    if resultado == 2:
        return True
    else:
        return False
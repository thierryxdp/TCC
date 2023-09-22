def primo(n):
    """dado um numero inteiro positivo, verifica se esse numero é primo ou nao"""
    numeros=1
    for numeros in range(1,n+1):
        if n%numeros==0:
            numeros= numeros+1
    if numeros==3:
        return True
    else:
        return False
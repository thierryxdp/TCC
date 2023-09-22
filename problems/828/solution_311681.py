def primo(n):
    """dado um numero inteiro positivo, verifica se esse numero é primo ou nao"""
    numeros2=1
    for numeros in range(1,n+1):
        if n%numeros==0:
            numeros2= numeros2+1
    if numeros2<=3:
        return True
    else:
        return False
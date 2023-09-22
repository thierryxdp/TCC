def primo(n):
    """Dado um número inteiro positivo, verifique se este número é primo ou não. Retorna um valor booleano.
    int-->int"""
    soma=0
    for numero in list(range(2,n-1)):
        if (n%numero)==0:
            soma=soma+1
    if soma ==0:
        return True
    else:
        return False
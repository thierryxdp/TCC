def primo(n):
    """Função que dado um número inteiro positivo, verifica se este número é primo ou não"""
    """int--->bool"""
    div=0
    for i in range(2,n,1):
        if n%i==0:
            return False
        else:
            return True
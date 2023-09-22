def primo(n):
    ''' retorna um valor booleano, dado um número inteiro positivo, verificando se este número é primo ou não;
    int->bool '''
    x = 0
    for elem in range(1, n+1):
        if n%x>0:
            x = x+1
        if n%x==0:
            x = x+1
            return False
        else:
            return True
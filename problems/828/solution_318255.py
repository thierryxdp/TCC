def primo(n):
    ''' retorna um valor booleano, dado um número inteiro positivo, verificando se este número é primo ou não;
    int->bool '''
    x = 0
    for elem in range(1, n+1):
        if n%elem>0:
            elem = elem + 1
        if n%elem==0:
            return False
        else:
            return True
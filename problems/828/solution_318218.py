def primo(n):
    ''' retorna um valor booleano, dado um número inteiro positivo, verificando se este número é primo ou não;
    int->bool '''
    x=0
    for elem in n:
        if n%elem!=0:
            return False
        if n%elem==0:
            return True
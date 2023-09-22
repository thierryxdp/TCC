def primo(n):
    ''' retorna um valor booleano, dado um número inteiro positivo, verificando se este número é primo ou não;
    int->bool '''
    
    for elem in len(n):
        if elem%2!=0:
            return False
        if elem%2==0:
            return True
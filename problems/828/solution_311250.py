def primo(n):
    '''dado um numero inteiro positivo n, essa funcao identifica se ele é primo ou nao
    int-->bool'''
    for i in range(2,n):
        if(n%i==0):
            return False
        elif(n/i<i):
            break
    return True
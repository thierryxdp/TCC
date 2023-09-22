def primo(n):
    '''funcao que verifica se o numero dado como entrada e primo ou nao
    int->bool'''
    for i in range(2,n):
        if n%i==0:
            return 'False'
    else:
        return 'True'
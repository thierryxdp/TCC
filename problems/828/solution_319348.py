def primo(x):
    '''Função que verifica se o número é primo ou não;
    Recebe um número;
    Retorna True ou False.'''
    if x==2 or x==3:
        return True
    for i in range(2,x):
        if (x%i)==0:
            return False
    return True
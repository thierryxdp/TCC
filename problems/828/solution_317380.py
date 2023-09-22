def primo(n):
    '''
    Funçao que verifica se um numero é primo
    int-> bool
    '''
    lista=[]
    if n == 2:
        return True
    else:
        for i in range(n):
            if n%i == 0:
                return False
            else:               
                return True
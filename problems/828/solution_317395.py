def primo(n):
    '''
    Funçao que verifica se um numero é primo
    int-> bool
    '''
    lista=[]
    if n == 2:
        return True
    elif n%(n**(1/2)) == 0:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            else:               
                return True
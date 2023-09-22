def primo(n):
    '''
    Funçao que verifica se um numero é primo
    int-> bool
    '''
    lista=[]
    if n == 2:
        return True
    else:
        for i in range(2,n):
            if (i**2) == n:
                return False
            elif n%i==0:
                return False
            else:               
                return True
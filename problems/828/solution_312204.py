def primo(n):
    '''funçao que determina se um número é primo'''
    # int > booleano
    if n > 1:
        for i in range(2,n):
            if (n%i)==0:
                return False
            else:
                return True
    else:
        return False
def primo(n:int)->bool:
    '''Diz se o número é primo ou não com True ou False'''
    i=2
    while i<n:
        if i%n==0:
            return False
        i+=1
        else:
            return True
def primo(numero):
    ''' '''
    i=0
    for i in range(2,numero):
        if numero % i==0:
            return False
        i+=1
        else:
            return True
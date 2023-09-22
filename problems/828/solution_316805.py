def primo(numero):
    ''' '''
    i=0
    for i in range(2,numero):
        if numero % i==0:
        i+=1
        if i>0:
            return False
        else:
            return True
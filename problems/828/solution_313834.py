def primo(n):
    ''' Função que identifica se n é um numero primo.
    int->booleano '''
    s=0
    for i in list(range(1,(n+1))):
        if(n%i==0 and i!=0):
            s=s+1
    if(s<2):
        return True
    elif(s>2):
        return False
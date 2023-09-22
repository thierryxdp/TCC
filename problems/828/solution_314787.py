def primo(num):
    '''Recebe um número e retorna True para 
    ele ser primo e False para não primo
    int->bool'''
    som=0
    for i in range(2,num):
        if num%i==0:
            som=som+1
    if som>0:
        return False
    else: 
        return True
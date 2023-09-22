def primo(n):
    ''' fuançao que recene um numero e retorna se ele e ou nao primo;
    int-> bool'''
    a=True
    for i in range(1,n):
        if n% i==0:
            a=False
        else:
            a= True
        
    return a
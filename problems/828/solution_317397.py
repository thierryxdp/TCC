def primo(n):
    '''Dado um número n, retorna True se ele é primo e False se não
    int->bool'''
    
    x=0
    
    if n<=2:
        return True 
    for i in range(1,n+1):
        if n%i==0:
            x=x+1
    if x==2:
        return True 
    else: 
        return False
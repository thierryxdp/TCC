def primo(num):
    '''Retorna True se o número de entrada
       é primo, e False se não for primo;
       int->bool'''
    i=0
    for n in range(1,num+1):
        if num%n==0:
            i+=1        
    if i==2:
        return True
    else:
        return False
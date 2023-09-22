def qtd_divisores(x):
    '''
    '''
    final=0
    
    for i in range(1,x):
        if x % i==0:
            final+=1
            
    if x<0:
        return final
    else:
        return final+1
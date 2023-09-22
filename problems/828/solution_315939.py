def primo(x):
    '''A função retorna como TRUE ou FALSE se o número informado é primo
    int -> bool'''
    
    y = []
    
    for numero in range(1,x+1):
        if x%numero == 0:
            list.append(y, numero)
            
    if len(y) <= 2:
        return 'True'
    else:
        return 'False'
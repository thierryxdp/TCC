def qtd_divisores(x):
    '''A função conta quantos divisores o número de entrada possui
    int - int'''
    
    y = []
    
    for numero in range(1,x+1):
        if x%numero == 0:
            list.append(y, numero)
    return len(y)
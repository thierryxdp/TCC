def repetidos (x):
    '''A função calcula a quantidade de repetições da lista informada
    lista -> int'''
    
    i = 0
    y = 0
    
    while len(x) > i:
        if x[i] == x[i-1]:
            y = y + 1
        i = i + 1
        
    return y
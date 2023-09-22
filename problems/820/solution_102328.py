def posLetra (x,y,z):
    '''A função retorna a posição da letra informada,
    caso houve menos ocorrência do que informado por z, a função retorna -1
    str, str, int -> int'''
    
    
    i = 0
    v = 0
    
    while len(x)>i:
        if x[i] ==  y:
            v = v + 1
        if x[i] == y and v == z:
            return i
        i = i + 1
        
    return -1
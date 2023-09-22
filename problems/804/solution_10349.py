def filtro_pares (a,b,c,d):
    '''recebe um tupla com 4 elementos inteiros e retorna'''
    '''int,int,int,int-> numeros pares'''
    numeros = a,b,c,d
    if a // 2 == 0:
        return [a]
    
    if b // 2 == 0:
        return [b]
    
    if c // 2 == 0:
        return [c]
    
    if d // 2 == 0:
        return [d]
    return [a]+[b]+[c]+[d]
def colchao(medidas,H,L):
    '''Retorna True se o colchao passara pela porta e False
    se ele não passara, dados as medidas em cm do colchao em 
    ordem crescente e as medidas da altura H e largura L da porta;
    list[float,float,float],int,int -> bool'''
    M = max(medidas)
    A = min(medidas)
    I = medidas[1]
    
    if ((M <= H) or (I <= H) or (I < L)) and (A < L):
        return True
    else:
        return False
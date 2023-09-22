def colchao(medidas, H, L):
    '''
    A função recebe: lista com as dimensões em ordem crescente e as 
    dimensões da porta (altura e largura). Se duas das dimensões forem
    menor que a porta, então o colchão conseguirá passar rotacionado.
    list, int, int -> bool    
    '''
    A = medidas[0]; B = medidas[1]; C = medidas[2]
    if (A<=H and B<=H) or (A<=L and B<=L): return True
    else: return False
def colchao(volume,H,L):
    '''
        funcao que retorna True se o colchao passa pelas portas e False em caso contrario.
        Teste de condição:
    if ordem[0] <= L and ordem[1] <= H:
        return True
    else:
        return False
        PARAMETROS:
        volume = list
        H = int 
        L = int
        ordem = list
        return Booleano 
    '''
    ordem = sorted(volume)
    if (ordem[0] <= L and ordem[1] <= H):
        return True
    elif ordem[1] <= H:
    	return True
    else:
        return False
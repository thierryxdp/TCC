def colchao(medidas, H, L):
    '''Função que retorna se, dadas as medidas AxBxC do colchão, a altura H e largura L das portas da casa do João, o colchão passa pelas portas ou não
    list, int, int -> bol'''
    
    if medidas[0] <= H and (medidas[1] <= L or medidas[2] <= L):
        return true
    
    elif medidas[1] <= H and (medidas[0] <= L or medidas[2] <= L):
        return true
    
    elif medidas[2] <= H and (medidas[0] <= L or medidas[1] <= L):
        return true
    
    else:
        return false
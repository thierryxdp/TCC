def colchao(medidas,H,L):
    '''todas as entradas sao inteiros medidos em cm'''
    #h é altura da porta
    # l largura da porta
    
    A= medidas[0]
    B=medidas[1]
    C=medidas[2]
    x = min( A ,min(B,C)) #menor
    y = min( max(A,B), max(B,C) , max (A,C) )# segundo menor
    if H < L:
        S=L
        V=H
    
    if x<L and y<H:
        return True
    
    elif x<V and y<S:
        return True
    else:
        return False
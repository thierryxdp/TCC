def colchao(medidas,H,L):
    '''Verifica se colchao(axBxC) passa pela porta(LxH)
          Obs.: ASSUME as dimensões do colchão
             ordenadas em ordem crescente
       [float,float,float],[float,float,float] -> bool'''

    lado1 = medidas[0]
    lado2 = medidas[1]
    lado3 = medidas[2]
    if H < L:
        porta = [H,L]
    else:
        porta = [L,H]
    
    X = min(lado1, lado2, lado3)
    Y = min(lado2,lado3)
    if(X <= L and Y <= H):
        return True
    else:
        return False
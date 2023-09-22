def colchao(medidas,H,L):
    '''função que retorna se o colchão passa pela porta da casa de 
    João ou não.
    lista, int, int -> boolean'''
    
    dim_colchao = medidas[0]*medidas[1]*medidas[2]
    dim_porta = H*L
    
    if dim_colchao>dim_porta:
        return False
    else:
        return True
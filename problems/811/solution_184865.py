def colchao(medidas,H,L):
    '''função que dada as dimensões do colchão,a altura da porta e a largura da porta, retorna se o colchão passa ou não, dando true ou false: list,int,int->bool'''
    A= lista[0]
    B= lista[1]
    
    if (B<=H and A<=L) or (B<=L and A<=H):
        return True
    else:
        return False
def colchao(medidas,H,L):
    """Função que determina se um colchão passa ou não passa pelas portas da casa de João; lista,int,int->booleano"""
    if((medidas[0] and medidas[1] and medidas[2]) > (H and L)):
        return False
    elif((medidas[1] and medidas[2]) > (H and L)):
        return False
    elif((int(medidas[1])*int(medidas[2]))>(H*L)):
        return False
    else:
        return True
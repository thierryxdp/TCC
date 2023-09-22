def colchao(medidas,H,L):
    """Função que determina se um colchão passa ou não passa pelas portas da casa de João; lista,int,int->booleano"""
    if(medidas[1] > H and medidas[1] > L) and (medidas[2] > H and medidas[2] > L):
        return False
    else:
        return True
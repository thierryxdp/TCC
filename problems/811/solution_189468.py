def colchao(medidas,H,L):
    """Função que determina se um colchão passa ou não passa pelas portas da casa de João; lista,int,int->booleano"""
    if(medida[1] > H and medida[1] > L) and (medida[2] > H and medida[2] > L):
        return False
    else:
        return True
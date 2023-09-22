def colchao (medidas,H,L):
    """Calcula e retorna a possibilidade ou não do colchao entrar na casa do Joao, dado a altura(h) e largura da porta(l) mais as dimensoes do colchão (a,b,c); float --> str"""
    
    if medidas[2]<=H and medidas[0]<=L:
        return 'True'
    elif medidas[2]>H and medidas[1]<=L:
        return 'True'
    elif medidas[1]<=H:
        return 'True'
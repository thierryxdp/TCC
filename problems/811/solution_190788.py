def colchao(medidas,H,L):
    """Funcao que retorna True se o colchao passar pela porta e False se o colchao nao passar
    list,int,int -> bool"""
    if medidas[1]>H and medidas[2]>L:
        return False
    else:
        return True
    if medidas[1]<L and medidas[2]<H:
        return True
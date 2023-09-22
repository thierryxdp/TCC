def colchao(medidas,H,L):
    """Funcao que retorna True se o colchao passar pela porta e False se o colchao nao passar
    list,int,int -> bool"""
    if medidas[1]>H or medidas[2]>L:
        return False
    esle:
        return True
def colchao(dimensoes,H,L):
    """retorna uma valor booleano que diz se o colchao passa pela porta ou nao;
    list,int,int -> bool"""
    if dimensoes[0]<=L and dimensoes[1]<=H:
        return True
    elif dimensoes[1]<=L and dimensoes[0]<=H:
        return True
    else:
        return False
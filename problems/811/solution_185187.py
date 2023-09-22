def colchao (colchao, altura, largura):
    """list, int, int -> bool"""
    dim = colchao
    dim.append(altura)
    dim.append(largura)
    dom.sort()
    altura_p = dim.count(altura) -1
    idx_porta_altura=dim.index(altura)+ altura_p
    largura_p = dim.count(largura) -1
    idx_porta_largura = dim.index(largura)+ largura_p
    return ((idx_porta_altura >0) and (idx_porta_largura >2)) or ((idx_porta_altura >2) and (idx_porta_largura>0))
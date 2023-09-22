def colisao(a,b):
    """Recebe duas tuplas contendo quatro coordenadas cartesianas
de dois vértices (inferior esquerdo e superior direito) e devolve
True se há colisão entre os retângulos ou False se não houver colisão.
tuple, tuple -> bool
"""
    largura_ret1 = modulo(a[2]-a[0])
    altura_ret1 = modulo(a[3]-a[1])
    largura_ret2 = modulo(b[2]-b[0])
    altura_ret2 = modulo(b[3]-b[1])
    if (a[0] < b[0] + largura_ret2 and
        a[0] + largura_ret1 > b[0] and
        a[1] < b[1] + altura_ret2 and
        a[1] + altura_ret1 > b[1]):
        return 0==0
    else:
        return 0==1
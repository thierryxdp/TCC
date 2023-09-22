def colchao(medidas,H,L):
    """Função  que calcula se um colchão passa por uma porta dados as medidas do colchão,
    a altura e a largura da porta respectivamente; list,int,int-->bool """
    x= medidas[0]
    y=medidas[1]
    if (y<=H and x<=L)or (y<=L and x<=H):
        return True
    else:
        return False
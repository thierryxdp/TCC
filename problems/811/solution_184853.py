def colchao(medidas,H,L):
    """Função  que calcula se um colchão passa por uma porta dados as medidas do colchão,
    a altura e a largura da porta respectivamente, """
    x= medidas[0]
    y=medidas[1]
    if (x<=H and y<=L)or (y<=L and x<=H):
        return True
    else:
        return False
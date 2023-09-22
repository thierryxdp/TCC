def colchao(medidas,H,L):
    """Função  que calcula se um colchão passa por uma porta dados as medidas do colchão,
    a altura e a largura da porta respectivamente, """
    x= medida[0]
    y=medida[1]
    if (H <= x and L<=y)or (H<=y and L<=x):
        return True
    else:
        return False
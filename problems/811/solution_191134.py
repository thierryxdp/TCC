def(medidas,H,L):
    '''Função que dado as medidas do colçhão, a altura da porta e a largura da porta  calcula se o colchão novo passa pela porta'''
    altura = medidas[1]
    largura = medidas[2]
    if largura<=L:
        return "True"
    elif altura<=H:
        return "True"
    else:
        return "False"
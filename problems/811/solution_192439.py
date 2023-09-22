def colchao(medidas, H, L):
    """Função que informa se o colchão passa pela porta, tendo a medida do colchão, a altura e largura da porta """
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    passoupelaporta= True

    if b>H and b>L:
        passoupelaporta= False
        return passoupelaporta
    if b<=H or b<=L:
        return passoupelaporta
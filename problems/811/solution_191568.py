def colchao(medidas,H,L):
"""Coloque as dimencoes do colchao entre [] acompanhado da altura e largura da porta separados por , exp:[25,120,220],200,100"""
    if medidas[0] <= L and medidas[1] <= H :
        print(True)
    else :
        print(False)
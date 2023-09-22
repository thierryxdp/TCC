def colchao(medidas,H,L):
    """Informe as medidas da cama entre [], e a altura e largura da porta separados por virgulas , exemplo: [25,120,220],200,100"""
    if medidas[0] <= L and medidas[1] <= H :
        return medidas[0] <= L
    else :
        return L > H
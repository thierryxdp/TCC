#Questão 7
def colchao(medidas,H,L):
    """calcula se de acordo com as dimensões da
porta, se é possivel passar o colchão
medidas - medidas da porta
H - altura do colchão ; L - largura do colchão"""
    return medidas[1]<=H and medidas[2]>=L
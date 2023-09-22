def colchao(medidas, altura, largura):
    "Verifique se um colchao com medidas determinadas passará por uma porta com dada altura e largura; float-> bool"
    if min(medidas[1:]) <=altura or min(medidas[1:]) <=largura:
        return True
    else:
        return False
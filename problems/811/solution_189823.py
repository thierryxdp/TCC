def colchao(medidas,H,L):
    espessura = medidas[0]
    largura = medidas[1]
    altura = medidas[2]
    if altura < H or altura < L:
        return True
    elif largura < H or largura < L:
        return True
    elif espessura < H or espessura < L:
        return True
    else:
        return False
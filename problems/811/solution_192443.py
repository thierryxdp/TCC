def colchao(medidas, H,L):
    medidas.sort()
    
    altura = medidas[0]
    largura = medidas[1]
    comprimento = medidas[2]
    
    if comprimento < H:
        return True
    elif largura < H:
        return True
    elif largura < L:
        return True
    else:
        return False
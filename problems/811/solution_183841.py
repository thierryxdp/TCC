''' A função diz se o cochão vai ser adquado ou não para joão'''
def colchao(medidas,H,L):
    if H>=medidas[1] or H>=medidas[2] or L>=medidas[1]:
        return True
    else:
        return False
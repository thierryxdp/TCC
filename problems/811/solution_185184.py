def colchao(medidas,H,L):
    '''scmsczx msjfks:
    lista, int, int -> bool'''
    altura = medidas[0]
    comprimento = medidas[1]
    largura = medidas[2]
    
    if (comprimento>H):
        if (largura>L):
            return False
        elif (largura<L):
            return True
        else:
            return True
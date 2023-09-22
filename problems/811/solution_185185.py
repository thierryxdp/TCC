def colchao(medidas,H,L):
    '''scmsczx msjfks:
    lista, int, int -> bool'''
    altura = medidas[0]
    comprimento = medidas[1]
    largura = medidas[2]
    
      if (comprimento_colchao>H):
        if (largura_colchao>L):
            return False
        else:
            return True
    elif (largura_colchao<L):
        return True
    else:
        return True
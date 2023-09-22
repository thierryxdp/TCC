def colchao(medidas, H, L):
    '''Retorna a possibilidade de se passar um colchao com dimensao dada por medidas por uma porta de dimensoes H e L'''
    #list, float, float -> bool
  

    if medidas[1] <= H or medidas[1] <= L:
        return True
    else:
        return False
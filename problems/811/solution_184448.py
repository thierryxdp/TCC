def colchao(medidas, H, L):
    '''Retorna a possibilidade de se passar um colchao com dimensao dada por medidas por uma porta de dimensoes H e L'''
    #list, float, float -> bool
  
 	B = medidas[1]
    if B <= H or B <= L:
        return True
    else:
        return False
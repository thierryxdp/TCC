def colchao(medidas,H,L):
    '''verifica se um colchao conseguirah passar por uma porta de medidas H e L
    list,int,int -> bool'''
    return True if medidas[1] <= L and medidas[2] <= H or medidas [2] <= L and medidas[1] <= H else return False
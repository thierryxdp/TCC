def colchao(medidas,H,L):
    '''verifica se um colchao conseguirah passar por uma porta de medidas H e L
    list,int,int -> bool'''
    saida = True if medidas[1] <= L and medidas[0] <= H or medidas [0] <= L and medidas[1] <= H else False
    return saida
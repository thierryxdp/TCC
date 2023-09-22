def colchao (medidas,H,L):
    '''Recebe uma lista com as dimensoes do colchao em centimetros (ordenadas de menor para maior), além dos
    parametros H(altura) e L(largura) em centimetros de uma porta e retorna True ou False dependendo se
    o colchao passa pela porta ou não
    list, float, float -> bool'''
    if medidas[1]<=H:
        return True
    else:
        return False
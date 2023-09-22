def colchao(medidas,H,L):
    '''funcao que calcula se e possivel um colchao passar por uma porta,na qual medidas e uma lista e H e L sao respectivamente altura e largura, retorna True se o colchao passa pela porta e False se nao'''
    lc=medidas[0]
    ac=medidas[2]
    cc=medidas[1]
    if cc <= H or cc <=L:
        return True
    elif ac <= H or ac<=L:
        return True
    elif lc<=L and lc<=H:
        return False
def colchao(medidas,H,L):
    '''funcao que dados os paremetros de entrada referentes as informacoes das medidas do colchao e da altura e largura de uma porta,
    retorna se e possivel atravessar o colchao pela porta
    list, int, int -> bool'''
    if medidas[0]<L and medidas[2]<H:
        return True 
    elif medidas[1]<L and medidas[2]<H:
        return True
    elif medidas[1]<L and medidas[0]<H:
        return True
    elif medidas[2]<L and medias[0]<H:
        return True
    else:
        return False
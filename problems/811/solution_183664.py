def colchao(med,H,L):
    '''dadas as medidas de um colchão, a altura e a largura de uma porta, retorna se o colchão passa ou não pela porta;
    list, int, int --> bool'''
    if H>L:
        return med[0]<L and med[1]<H
    else:
        return med[0]<H and med[1]<L
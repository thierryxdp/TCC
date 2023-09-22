def colchao(medidas,H,L):
    '''calcula e retorna se o colchão passa ou não pela porta;
list,int,int->bool'''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    alt_da_porta = H
    larg_da_porta = L
    if (A<=H and B<=L) or (A<=H and C<=L) or (B<=H and C<=L) or (B<=H and A<=L) or (C<=H and A<=L) or (C<=H and B<=L):
        return True
    else:
        return False
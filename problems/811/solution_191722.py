def colchao(medidas,H,L):
    ''' dada uma lista(medidas) com as dimensões em cm, ordenadas de menor para maior, e aos números inteiros da altura H e da largura L da porta em cm, retorna True se o colchão conseguir passar e false, caso contrário;
    list,int,int->bool '''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<=H and B<=L:
        return True
    elif A<=H and C<=L:
        return True
    if B<=H and C<=L:
        return True
    elif C<=H and B<=L:
        return True
    if A<=L and C<=H:
        return True
    elif A<=L and B<=H:
        return True
    else:
        return False
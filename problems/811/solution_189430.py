def colchao(medidas,H,L):
    '''compara a altura do colchão com a da porta e diz se passa
    ou a largura do colchão com a da porta e diz se passa
    caso contrario retorna que não passa'''
    '''list,int,int->bool'''
    col=medidas[1]
    por=H
    por2=L
    col2=medidas[2]
    if por>col:
        return True
    elif por==col:
        return True
    if por2>col2:
        return True
    else:
        return False
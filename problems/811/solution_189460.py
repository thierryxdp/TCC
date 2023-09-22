def colchao(medidas,H,L):
    '''compara a altura do colchão com a da porta e diz se passa
    ou a largura do colchão com a da porta e diz se passa
    caso contrario retorna que não passa'''
    '''list,int,int->bool'''
    colchao=medidas[1]
    por=H
    por2=L
    colchao2=medidas[2]
    if por>colchao:
        return True
    elif por==colchao:
        return True
    if por2>colchao2:
        return True
    else:
        return False
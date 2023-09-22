colchao(medidas,H,L):
    '''Funcao que retorna
ent->lista, int, int
saida->boo'''
    menor_colchao=medidas[0]
    menor2_colchao=medidas[1]
    porta_dimens_menor= min(H,L)
    porta_dimens_maior= max(H,L)
    if menor_colchao <= porta_dimens_menor and menor2_colchao <= porta_dimens_maior:
        return True
    else:
        return False
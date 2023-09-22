def colchao(medidas,H,L):
    '''Função que, dadas as medidas do colchão (ordenadas de forma crescente), a altura H e a largura L da porta, retorna True se o colchão passa pela porta e False caso contrário.
list,float,float --> bool'''
    if medidas[0]<=L and medidas[1]<=H:
        return True
    else:
        return False
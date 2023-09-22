def colchao(medidas,H,L):
    '''Dadas as medidas do colchão e a altura e largura da porta, a função define se João conseguirá passar o colchão pelas portas da sua casa
    int,int,int->bool'''
    if medidas[1]<=H:
        return True
    else:
        return False
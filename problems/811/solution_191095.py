def colchao(medidas,H,L):
    '''Recebe uma lista com as medidas de um colchão em prdem crescente e as medidas de uma porta e devolve se é possível passar com o colchão através dela;
    	list, num, num -> bool'''
    if medidas[0]<=H and medidas[1]<=L:
        return True
    if medidas[0]<=H and medidas[2]<=L:
        return True
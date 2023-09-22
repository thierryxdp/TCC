def colchao (medidas,H,L):
    '''funcao que recebe as medidas de um colchao
    	e analisa se ele passa na porta
        H-> int altura
        L-> int largura
        return: bool
    '''
    [A,B,C] = medidas
    A<B<C
    if B > H and C > L:
        return False 
    else:
        return True
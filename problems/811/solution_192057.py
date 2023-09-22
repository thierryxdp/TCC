def colchao(medidas,H,L):
    '''Função para saber se consegue passar o colchão 
    pela porta ou não. list, int -> bool'''
    [A,B,C] = medidas
    if medidas[1] <= H:
        return True
    else:
        return False
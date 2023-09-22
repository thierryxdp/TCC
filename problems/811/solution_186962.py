def colchao(medidas,H,L):
    '''função que retorna se de acordo com as medidas '''
    if medidas[1]<=H or medidas[1]<=L :
        return True
    else:
        return False
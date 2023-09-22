def colchao(medidas,H,L):
    '''resolve o problema para que o colcão passe atraves das portas de medida HxL'''
    medidas = [medidas[0], medidas[1], medidas[2]]
    if medidas[1]<=H or L>=medidas[2]:
        return True
    else:
        return False
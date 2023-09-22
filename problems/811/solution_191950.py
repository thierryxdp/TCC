def colchao(med,H,L):
    ''' funcao retorna um boleano com as certas medidas'''
    
    if med[1] <= H:
        return True
    if med[1] <= L:
        return True
    if
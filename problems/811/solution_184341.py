def colchao (medidas,H,L):
    '''Funcao que descobre se um colchao dado suas medidas, passa pela 
    porta da casa de uma pessoa, de acordo com sua medida (porta)
    int+int+int - > bool'''
    
    if H >= medidas [1]:
        return True
    if H >= medidas [2]:
        return True
    
    else:
        return False
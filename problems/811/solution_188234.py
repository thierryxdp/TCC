def colchao (m,h,l):
    '''retorna se o colchão é capaz de passar pela porta ou não
    a partir dos termos m (medidas), h (altura) e l (largura)'''
    mat = m
    por = h,l
    if (mat[0] <= por[1] and mat[1] <= por[0]) or (mat[0] <= por[0] and mat[1] <= por[1]):
        return True
    else:
        return False
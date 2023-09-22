def colchao(medidas,H,L):
    '''retorna se o colchao passa ou nao em uma porta;
    float->bool'''
    f=medidas
    if f[1]<=H or f[1]<=L:
        return True 
    elif f[2]<=H or f[2]<=L:
        return True
    else:
        return False
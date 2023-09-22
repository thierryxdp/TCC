def eh_quadrada(m):
    '''retorna true ou false se for ou não matriz quadrada'''
    m = []
    l=len(m)
    c=len(m[0])
    matriz[l][c]=int(input(f'valor para [{l},{c}]:'))
    if len([l])==len([c]):
        return True
    else:
        return False
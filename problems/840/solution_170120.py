def bolos(xicara,ovos,colheres):
    '''calcula a quantidade máxima de bolos que João consegue fazer'''
    a = xicara // 2
    b = ovos // 3
    c = colheres // 5
    return min(a,b,c)
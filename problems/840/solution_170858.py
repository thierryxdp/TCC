def bolos(A,B,C):
    '''calcula a quantidade maxima de bolos que podem ser feitos a partir dos ingredientes A,B,C'''
    qtd = ((A//2),(B//3),(C//5))
    limite = min(qtd)
    return limite
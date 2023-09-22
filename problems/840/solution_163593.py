def bolos(A,B,C):
    '''calcula e retorna o numero maximo de bolos que poderao ser feitos com A xicaras,B ovos e C colheres'''
    return min((A//2),(B//3),(C//5))
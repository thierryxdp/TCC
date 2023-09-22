def bolos(a,b,c):
    '''Inseridos o número de xícaras de leite recebidas, o número de ovos, e o número de colheres de leite (a,b,c), retorna o número exato de bolos que pode ser feito'''
    return min(a//2, b//3, c//5)
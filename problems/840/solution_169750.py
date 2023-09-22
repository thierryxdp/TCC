def bolos(A,B,C):
    '''Esta função calcula a quantidade de bolos que João pode
    fazer de acordo com  a quantidade disponível de cada material,
    sendo as entradas A=farinha de trigo, B=ovo e C=colheres de
    sopa de leite'''
    return min(A//2,B//3,C//5)
def bolos(A,B,C):
    ''' função que calcula a quantidade máxima de bolos inteiros que da para fazer dados a quantidade de xícaras de farinha de trigo, de ovos e de colheres de sopa de leite que se tem visto que necessitam de 2,3 e 5 dos ingredientes,respectivamente, para a produção de 1 bolo'''
    return min(A//2,B//3,C//5)
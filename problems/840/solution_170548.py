def bolos(A,B,C):
    '''funcao que calcula a quantidade maxima de bolos
    que Joao consegue fazer dados a quantia de ingredientes,
    sendo A as xicaras,B os ovos e C as colheres de sopa de leite.'''
    x = min(A//2, B//3, C//5) #x é a quantidade de bolos.
    return x
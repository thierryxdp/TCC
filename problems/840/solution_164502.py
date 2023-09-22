def bolos(A,B,C):
    '''calcula e retorna quantas receitas inteiras de bolo podem ser feitas
    com A xicaras de farinha, B ovos e C colheres de sopa de leite
    float, float -> int'''
    return min(A//2,B//3,C//5)
def bolos(A,B,C):
    '''calcula e retorna o numero máximo de bolos  
    que se pode cozinhar, dadas as quantidades disponíveis de 
    farinha de trigo, ovos e sopa de leite
    A - xícaras de farinha de trigo
    B - unidades de ovos
    C - colheres de sopa de leite;
    float, int, float -> int'''
    return min((A//2),(B//3),(C//5))
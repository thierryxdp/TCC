def bolos(xicaras_farinha,ovos,colheres_leite):
    '''calcula e retorna a quantidade maxima de bolos que 
    podem ser feitos por Joao dadas as quantidades de cada
    ingrediente
    int, int, int -> int'''
    return min(xicaras_farinha//2,ovos//3,colheres_leite//5)
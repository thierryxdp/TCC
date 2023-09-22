def bolos(xicaras_trigo,ovos,colheres_leite):
    '''calcula e retorna a quantidade maxima de bolos que Joao consegue fazer dadas as quantidades de igredientes disponiveis'''
    return min(xicaras_trigo//2,ovos//3,colheres_leite//5)
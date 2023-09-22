def num_de_bolos(xicaras_trigo,ovos,colheres_leite):
    '''calcula e retorna a quantidade maxima que Joao consegue fazer dadas as quantidades de igredientes disponiveis
    int, int, int -> int'''
    return min(xicaras_trigo//2,ovos//3,colheres_leite//5)
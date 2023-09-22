def bolos (trigo, ovos, leite):
    ''' calcula a quantidade máxima de bolos possível 
    int, int, int => int'''
    qtd_farinha = farinha//2
    qtd_ovos = ovos//3
    qtd_leite = leite//5

    return min(trigo, ovos, leite)
def bolos(farinha, ovos, leite):
    ''' Retorna a quantidade maxíma de bolos que é possível fazer dados
    a quantidade de xícaras de (farinha), quanitade de (ovos),
    e colheres de leite (leite)
    int, int, int -> int
    '''
    
    #Quantida mínima de bolos por ingrediente.
    min_farinha = farinha // 2;
    min_ovos = ovos // 3;
    min_leite = leite // 5;
    
    return min(min_farinha, min_ovos, min_leite);
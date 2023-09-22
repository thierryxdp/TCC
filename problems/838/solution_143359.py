def num_bombons(D, P):
    '''funçao calcula o numero maximo de bombons que pedrinho consegue comprar com o dinheiro que possui;
    float, float -> float'''
    return max(D // P)>1
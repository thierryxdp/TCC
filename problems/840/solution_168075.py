def bolos(A,B,C):
    '''Função que calcula e retorna a quantidade máxima de bolos 
    que pode fazer com a quantidae de ingredientes dada;
    int, int, int -> int'''
    quant_min_farinha = A//2
    quant_min_ovos = B//3
    quant_min_colher_leite = C//5
    return min(quant_min_farinha, quant_min_ovos, quant_min_colher_leite)
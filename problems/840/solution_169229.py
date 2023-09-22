def bolos(A,B,C):
    '''calcula a quantidade maxima de bolos que podem ser 
    feitos, dados seus ingredientes'''
    quant_farinha=2
    quant_ovos=3
    quant_leite=5
    return min(quant_farinha,quant_ovos,quant_leite)
def bolos(A,B,C):
    '''calcula a quantidade maxima de bolos que podem ser 
    feitos, dados seus ingredientes'''
    quant_farinha=A//2
    quant_ovos=B//3
    quant_leite=C//5
    return min(quant_farinha,quant_ovos,quant_leite)
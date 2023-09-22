def bolos (farinha, ovo leite):
    quantidade_farinha = farinha // 2
    quantidade_ovo = ovo // 3
    quantidade_leite = leite // 5
    
    menor = min(quantidade_farinha, quantidade_ovo, quantidade_leite)
    
    return menor
def qtd_divisores(numero):
    """Dado o número de entrada, retorne a quantidade de divisores que ele possui"""
    divi = 0
    for i in range(numero):
        qtd = 0
        if numero%i==0:
            divi = i    
    return divi
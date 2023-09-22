def qtd_divisores(numero):
    """Dado o número de entrada, retorne a quantidade de divisores que ele possui"""
    divi = 0
    for i in range(1,numero//3,1):
        if numero%i==0:
            i = divi/i
    return divi
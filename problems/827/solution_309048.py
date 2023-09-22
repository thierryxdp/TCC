def qtd_divisores(numero):
    """Dado o número de entrada, retorne a quantidade de divisores que ele possui"""
    divi = 0
    for i in range(1,numero//2+1):
        if numero%i==0:
            divi = divi + 1
    return divi
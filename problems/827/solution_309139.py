def qtd_divisores(numero):
    """Dado o número de entrada, retorne a quantidade de divisores que ele possui"""
    divi = 0
    i = 1
    for i in range(1,numero//3):
        if numero%i==0:
            i = i + 1
            divi = i
    return divi
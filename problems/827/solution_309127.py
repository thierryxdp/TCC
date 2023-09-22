def qtd_divisores(numero):
    """Dado o número de entrada, retorne a quantidade de divisores que ele possui"""
    divi = 0
    for i in range(1,numero//3):
        if numero%i==0:
            divi = (divi + i)+1
    return divi
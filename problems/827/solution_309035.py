def qtd_divisores(numero):
    """Dado o número de entrada, retorne a quantidade de divisores que ele possui"""
    divi = 0
    for i in range(numero):
        if numero%i==0:
            divi= i
        divi = divi + len(numero%i==0)
        
    return divi
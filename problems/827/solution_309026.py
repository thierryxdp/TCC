def qtd_divisores(numero):
    """Dado o número de entrada, retorne a quantidade de divisores que ele possui"""
    divi = 0
    for i in range(1,numero,1):
        if numero%i==0:
            divi = i
        str.count(numero%i==0,i)    
    return divi
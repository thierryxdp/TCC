def fatorial(numero):  
    """Função que dado um numero retorna o fatorial desse numero 
    int --> int """
    fator = 1
    while numero in range(1,numero+1):
        fator=fator*numero
    return fator
def qnt_divisores(numero):
    """Função que calcula e retorna quantos divisores um número tem"""
    """Parâmetros de entrada:int"""
    """Parâmetros de saída:int"""
    acumulador=0
    for elemento in range(1,numero+1):
        if numero%elemento==0:
            acumulador+=1
    return acumulador
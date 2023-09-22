def qnt_divisores(numero):
    """Função que calcula e retorna quantos divisores um número tem"""
    """Parâmetros de entrada:int"""
    """Parâmetros de saída:int"""
    acumulador=0
    contador=1
    while contador <= numero:
        if numero%contador==0:
            acumulador+=1
    contador+=1
    return acumulador
def qtd_divisores(numero):
    """dado um inteiro numero de entrada,
    retorna o número de divisores que esse numero tem
    int --> int"""
    divisores=[]
    for n in range(1,numero+1):
        if numero%n==0:
            divisores=divisores+[n]
    return len(divisores)

def primo(inteiro_positivo):
    """dado um numero inteiro positivo de entrada,
    retorna um booleano True se o numero for primo e do contrário False
    int --> bool"""
    if qtd_divisores(inteiro_positivo)==2:
        return True
    else:
        return False
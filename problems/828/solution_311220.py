def primo(numero):
    """Função que dado um numero de entrada identifica se é primo ou não
    int -> bool"""
    divisores = 0
    for i in range(1,numero+1):
        if numero%i ==0:
            divisores=divisores+ 1
    if divisores == 2:
        return True
    else:
        return False
def primo(num):
    """funcao que dado um numero inteiro positivo, verifica se ele é primo ou nao
    int--->bool"""
    for elem in range(2,num):
        if num%elem==0:
            return False
    return True
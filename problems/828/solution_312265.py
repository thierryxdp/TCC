def qtd_divisores(num):
    """Conta o número de divisores que um dado número tem
    int -> int"""
    divisores = 0
    for i in range(1, num+1):
        if num%i == 0:
            divisores += 1
    return divisores

def primo(num):
    """Recebe um número inteiro positivo e verefica se este é primo. Caso seja,
    retorna trua, caso contrário False.
    int -> bool"""
    divisores = qtd_divisores(num)
    if divisores == 2:
        return True
    else:
        return False
def qtd_divisores(num):
    divisores = 0
    for numeros in range(1,num+1):
        if num%numeros == 0:
            divisores += 1
    return divisores



def primo(num):
    if qtd_divisores(num) > 2 or 1:
        return False
    if qtd_divisores(num) == 2:
        return True
def qtd_divisores(num):
    """Essa função serve para calcular quantos divisores um número tem
    int->int"""
    divisores = 0
    for numeros in range(1,num+1):
        if num%numeros == 0:
            divisores += 1
    return divisores

#qtd_divisores(67) == 2
#qtd_divisores(12) == 6
#qtd_divisores(13) == 2

def primo(num):
    """Essa função serve para dizer se o número é primo ou não
    int->bool"""
    if qtd_divisores(num) == 2:
        return True
    if qtd_divisores(num) > 2 or 1:
        return False

#primo(67) == True
#primo(12) == False
#primo(13) == True
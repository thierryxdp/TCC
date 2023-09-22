def qtd_divisores(num):
    divisores = 0
    for numeros in range(1,num+1):
        if num%numeros == 0:
            divisores += 1
    return divisores

def primo(num):
    '''função que recebe um inteiro e diz se o número é primo ou não
    int->bool'''
  
    if qtd_divisores(num) == 2:
        return True
    if qtd_divisores(num) > 2 or 1:
        return False
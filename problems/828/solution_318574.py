def primo(num):
    '''função que recebe um inteiro e diz se o número é primo ou não
    int->bool'''
    
    if qtd_divisores(num) == 2:
        return True
    if qtd_divisores(num) > 2 or 1:
        return False
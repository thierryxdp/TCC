def qtd_divisores(num):
    '''Retorna a quantidade de divisores de um número
    int -> int '''
    divisores = 0
    for x in range(1,num+1):
        if num%x ==0:
            divisores = divisores + 1
    return divisores

def primo(num):
    '''Dado um número inteiro positivo, verifica se este número
    é primo ou não, retornando True se for primo e False se não
    for
    int -> bool'''
    if qtd_divisores(num) == 2:
        return True
    else:
        return False
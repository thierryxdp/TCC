def qtd_divisores(num):
    '''Retorna a quantidade de divisores dado um numero
    int -> int '''
    divisores = 0
    for x in range(1,num+1):
        if num%x ==0:
            divisores = divisores + 1
    return divisores

def primo(num):
    '''Retorna true caso primo e false caso nao primo dado um numero inteiro positivo
    int -> bool'''
    if qtd_divisores(num) == 2:
        return True
    else:
        return False
def qtd_divisores(num):
    ''' função que retorna a quantidade de divisores de um número
    int --> int '''
    divisores = 0
    for x in range(1,num+1):
        if num%x ==0:
            divisores = divisores + 1
    return divisores

def primo(num):
    ''' função que retorna True se o número for primo e False se não
    for, dado como parâmetro um número inteiro positivo
    int --> bool'''
    if qtd_divisores(num) == 2:
        return True
    else:
        return False
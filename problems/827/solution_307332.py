def qtd_divisores(num):
    '''Retorna a quantidade de divisores de um número
    int -> int '''
    divisores = 0
    for x in range(1,num+1):
        if num%x ==0:
            divisores = divisores + 1
    return divisores
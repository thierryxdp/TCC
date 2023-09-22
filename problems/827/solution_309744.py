def qtd_divisores(num):
    '''
    função que conta a quantidade de divisores
    de um determinado numero
    int -> int
    '''
    i = 0
    for caractere in range (1,num+1):
        if num % caractere == 0:
            i = i + 1
    return i
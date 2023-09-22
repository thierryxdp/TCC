def qtd_divisores(numero):
    '''Retorna quantos divisores tem um número, recebe como
    parâmetro o número a ser verificado dado pelo usuário;
    Int-->Int.'''
    divisores=0
    for var in range(1,numero+1):
        if numero%var==0:
            divisores+=1
    return divisores
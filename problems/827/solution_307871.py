def qtd_divisores(num):
    '''Função que dado um numero inteiro de entrada, 
    retorna quantos divisores este numero possui;
    int-->int'''
    cont = 1
    if num < 0:
        cont = 0
    for i in range(1, num):
        if num%i == 0:
            cont = cont + 1
    return cont
def qtd_divisores(numero):
    '''dado um numero inteiro, a funçao nos devolve o 
    numero de divisores inteiros desse numero
    int-->int'''
    soma=0
    for i in range(numero):
        if numero%(i+1)==0:
            soma=soma+1
    return soma
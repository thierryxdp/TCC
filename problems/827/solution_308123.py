def qtd_divisores(n):
    '''Esta e a funcao que dado um numero inteiro,
    conta quantos divisores este mesmo numero possui'''
    contador=0
    for i in range(1,n+1):
        if (n % i) == 0:
            contador+=1
    return contador
def qtd_divisores(n):
    '''funcao que, dado um numero de entrada, retorna a quantidade de divisores positivos
    desse numero;
    float->int'''
    qtd=0
    for i in range(1,n+1):
        if (n % i) == 0:
            qtd = qtd + 1
    return qtd
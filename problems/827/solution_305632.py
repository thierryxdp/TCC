def qtd_divisores(n):
    '''retorna a quantidade de divisores o numero inteiro n tem;
    int->int'''
    resultado = 0
    for i in range(1,n+1):
        if n%i == 0:
            resultado = resultado + 1

    return resultado
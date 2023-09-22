def qtd_dividores(n):
    '''Funcao que retorna a quantidade de divisores que o numero de
    entrada possui. int->int'''
    soma=0
    divisores=range(1,10000)
    for x in divisores:
        if n%x==0:
        soma=soma+1
    return soma
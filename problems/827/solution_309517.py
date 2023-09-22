def qtd_divisores(n):
    '''Função que retorna a quantidade de divisores de um número, dado um número n;float->int'''
    quant_divisores=0
    fim=n+1
    for a in range(1,fim):
        if (n%a==0) and ((n/a)>=1):
            quant_divisores=quant_divisores+1
    return quant_divisores
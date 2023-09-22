def qtd_divisores(num):
    '''Função que retorna a quantidade de divisores que um numero tem.
    int->int'''
    quant_divisores=0
    for possivel_divisor in range(1,num+1):
        if num%possivel_divisor==0:
            quant_divisores+=1
    return quant_divisores
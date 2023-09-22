def qtd_divisores(n):
    '''Função que retorna a quantidade de divisores de um número, dado um número n;float->int'''
    quant_divisores=0
    divisor=[1,n,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]	
    for a in divisor:
        if (n%a==0) and ((n/a)>=1):
            quant_divisores=quant_divisores+1
    return quant_divisores
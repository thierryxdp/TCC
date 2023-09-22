def qtd_divisores(n):
    '''funcao que recebe como parametro um numero n e 
    retorna a quantidades de divisores que esse numero tem
    float->int'''
    divisores=0
    for elementos in range(n):
        if n/elementos==0:
            divisores = divisores + 1
    return divisores
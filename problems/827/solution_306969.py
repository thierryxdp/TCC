def qtd_divisores(numero):
    '''função que recebe como entrada um número inteiro e retorna o número de
divisores que esse numero inteiro possui; int->int'''

    divisores=0
    for x in range(1,numero+1):
        if numero%x==0:
            divisores=divisores+1
    return divisores
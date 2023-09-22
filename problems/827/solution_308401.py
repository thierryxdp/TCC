def qtd_divisores(numero):
    '''conta a quantidade de divisores o número apresentado tem. int->int'''
    divisores=0
    numeros_dividir= list(range(1,numero+1))
    for i in numeros_dividir:
        if numero % i == 0:
            divisores+=1
    return divisores
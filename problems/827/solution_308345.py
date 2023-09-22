def qtd_divisores(numero):
    'recebe um numero e retorna a quantidade de divisores que ele tem'
    quantidade=0
    for divisor in range(numero+1):
        if divisor !=0 and numero % divisor==0:
            quantidade+=1
    return quantidade
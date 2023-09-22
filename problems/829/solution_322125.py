def soma_h(n):
    """funcao que calcula e retorna o valor de h, que é a soma de 1 divido por todos os inteiros até n;
       int->float"""
    soma=0
    for i in range(1,n+1):
        soma=soma+1/i
    return round(soma,2)
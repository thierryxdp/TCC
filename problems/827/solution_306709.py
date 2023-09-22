def qtd_divisores(numero):
    """funcao que calcula e retorna a quantidade de divisores de um numero;
       int->int"""
    divisores=[]
    for i in range(1,numero+1):
        if numero%i==0:
            divisores=divisores+[i,]
    return len(divisores)
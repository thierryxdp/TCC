def qtd_divisores(numero):
    """funcao que calcula a quantidade de divisores de um numero"""
    divisores=[]
    for x in numero:
        if int(numero[0])%x==0:
            divisores=divisores+x
    return len(divisores)
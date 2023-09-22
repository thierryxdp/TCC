def qtd_divisores(numero):
    """funcao que calcula a quantidade de divisores de um numero"""
    divisores=[]
    for x in range(1,numero+1):
        if numero%x==0:
           divisores= divisores + [x] + [numero] 
    return len(divisores)
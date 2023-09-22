def qtd_divisores(numero):
    """funcao que retorna a quantidade de divisores do numero de entrada;
    int -> int"""
    divisores=0
    for n in range(1,numero+1):
        if numero%n==0:
            divisores=divisores+1
    return divisores
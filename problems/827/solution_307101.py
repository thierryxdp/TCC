def qtd_divisores(x):
    """ Função que retorna o número de divisores que x tem
    int -> int """
    divisores=0
    for numero in range(1,x+1):
        if x%numero==0:
            divisores=divisores+1
    return divisores
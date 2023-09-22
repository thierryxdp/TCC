def qtd_divisores(x):
    """ Função que retorna o número de divisores que x tem
    int -> int """
    i=1
    divisores=0
    while i<=x:
        if x%i==0:
            divisores=divisores+1
    return divisores
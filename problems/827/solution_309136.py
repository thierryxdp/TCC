def qtd_divisores(numero):
    '''
    Função que retorna quantos divisores um numero(numero) tem
    int -> int
    '''
    divisores=0
    for i in range(numero):
        if i//numero==0:
            divisores=divisores+1
    return divisores
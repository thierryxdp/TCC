qtd_divisores(numero):
    '''
    retorna quantos divisores o numero em questao tem
    int -> int
    '''
    div=0
    for num in range(1,numero+1):
        if numero%num==0:
            div+=1
    return div
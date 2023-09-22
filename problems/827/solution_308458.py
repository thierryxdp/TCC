def qtd_divisores(N):
    '''Uma funcao que conta quantos divisores um numero tem
    int -> int'''
    quantidade = 0
    for i in range(N):
        if N%(i+1)==0:
            quantidade += 1
    return quantidade
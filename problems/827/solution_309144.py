def qtd_divisores(numero):
    '''
    Função que retorna quantos divisores um numero(numero) tem
    int -> int
    '''
    divisores=0
    for i in range(1, numero//2+1):
        if numero % i ==0:
            divisores+=1
    return divisores+1
def qtd_divisores(numero):
    '''
    Função que retorna quantos divisores um numero(numero) tem
    int -> int
    '''
    divisores=0
    for i in range(1, numero//2+1):
        if numero % i ==0:
            divisores+=1
    if divisores==0:
        return 0
    elif divisores!=0:
        return divisores+1
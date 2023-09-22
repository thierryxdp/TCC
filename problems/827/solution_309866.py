def qtd_divisores(numero):
    '''função que retorna quantos divisores
    um número tem
    float -> int'''
    
    divisores = 0
    for i in range (1,numero+1) :
        if numero % i == 0 :
            divisores +=1
    return divisores
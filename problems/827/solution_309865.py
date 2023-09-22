def qtd_divisores(numero):
    '''função que retorna quantos divisores
    um número tem
    float -> int'''
    
    cont = 0
    for i in range (1,numero+1) :
        if numero % i == 0 :
            cont +=1
    return cont
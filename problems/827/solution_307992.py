def qtd_divisores(numero):
    '''recebe um numero como entrada e retorna quantos
    divisores esse numero tem
    int->int'''
    lista=list(range(1,numero+1))
    divisores=[]
    for elemento in lista:
        if numero%elemento==0:
            divisores=divisores+[elemento]
    return len(divisores)
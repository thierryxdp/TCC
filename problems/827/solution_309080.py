def qtd_divisores(numero):
    '''funcao que calcula quantos divisores um numero dado como entrada tem
    int->int'''
    soma=0
    for i in range(1,numero,1):
        if numero%i==0:
            soma=i+1
    return soma
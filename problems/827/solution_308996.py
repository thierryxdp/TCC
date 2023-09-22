def qtd_divisores(numero):
    '''funcao que calcula quantos divisores um numero dado como entrada tem
    int->int'''
    soma=0
    for i in numero:
        if numero%i==0:
            soma=soma+i
    return soma
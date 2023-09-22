def qtd_divisores(numero):
    '''Função que recebe um número e retona a quantidade de divisores
    que ele possui. int->int'''
    divisores=[]
    for i in range (1,numero+1):
        if numero%i==0:
            list.append[divisores,i]
    return len(divisores)
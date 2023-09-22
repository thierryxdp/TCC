def qtd_divisores(numero):
    '''Função que recebe um número e retona a quantidade de divisores
    que ele possui. int->int'''
    divisores=[]
    for i<=numero:
        if numero%i==0:
            divisores.append[i]
    return len(divisores)
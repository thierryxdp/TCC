def qtd_divisores(numero):
    '''Função que recebe um número e retona a quantidade de divisores
    que ele possui. int->int'''
    resposta = 0
    for i in range (1,numero+1):
        if numero%i==0:
            resposta = resposta +1
    return resposta
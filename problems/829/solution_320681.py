def soma_h(n):
    '''Função que calcula e retorna o valor de h com n termos, onde n é o inteiro dado como parametro de entrada; int->int'''
    soma=0
    for x in list(range(1,n+1)):
        soma=soma+1/x
    return round(soma,2)
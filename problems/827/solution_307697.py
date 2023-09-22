def qtd_divisores(numero):
    '''Função que calcula e retorna a quantidade de divisores de um número inteiro
    dado como entrada; int->int'''
    quantidade=0
    for i in range(1,numero+1):
        resto= numero%i
        if resto == 0:
            quantidade+=1
        else:
            quantidade = quantidade
    return quantidade
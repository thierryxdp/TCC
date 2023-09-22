def soma_h(numero):
    '''Função que calcula a soma de todos os termos de uma
    lista H de N termos dado um N inteiro como entrada do 
    parâmetro
    int ->float'''
    soma=0
    for i in range(1,numero+1):
        soma=soma+1/i
    return round(soma,2)
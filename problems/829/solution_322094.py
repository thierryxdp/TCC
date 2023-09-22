def soma_h(numero):
    '''Função que retorna a soma inversas dos números de 1 até numero;
    recebe como parâmetro o número a ser trabalhado; Int-->float'''
    soma=1
    for var in range(2,numero+1):
        soma=soma+(1/var)
    return round(soma,2)
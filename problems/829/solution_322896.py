def soma_h(N):
    '''calcule uma funcao que retorne o valor da soma H com N 
    termos onde N é inteiro e dado como entrada. int-->float'''
    soma = 0
    for i in range(1,N+1):
        soma = soma + (1/i)
    return round(soma,2)
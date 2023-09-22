def soma_h(N):
    '''função que calcula e retorna o valor de H com N termos, onde N e dado como parâmetro. retorna o resultado com somente duas casas decimais. int -> float'''
    soma = 0
    for x in range(1,N+1):
        soma = soma + 1/x
    return round(soma,2)
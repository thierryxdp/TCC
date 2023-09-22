def soma_h(N):
    ''' função que define o valor da soma da divisão de 1 até 1/N de N termos ( 1 + 1/2 + 1/3 + 1/4 ... 1/n )
        int ---> float '''
    soma = 0
    for a in range (1,N+1):
        b = 1/a
        soma = soma + b
        a +=1
    return round(soma,2)
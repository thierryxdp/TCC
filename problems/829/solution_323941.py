def soma_h(N):
    '''
    função que calcula o valor H com N termos, onde N é dado como entrada. 
    Obs: N é inteiro 
    int->float 
    
    '''
    
    soma = 0
    for k in range(1, N + 1):
        inverso = (1/k)
        soma=soma+inverso
    return round(soma, 2)
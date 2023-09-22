def soma_h(N):
    '''
    Função que calcula o valor H com N termos, onde N é um inteiro dado como entrada. 
    int-> int
    '''
    
    soma = 0
    for k in range(1, N + 1):
        inverso = (1/k)
        soma=soma+inverso
    return round(soma, 2)
def soma_h(N):
    '''Função que retorna o valor de H com N termos, onde N é inteiro
    	e dado como entrada, a partir da fórmula: H=1+1/2+1/3+...+1/N
   		retornando o valor dessa soma com apenas 2 casa decimais
        
        int -> float'''
    H=0
    for i in range(N):
        H=H+1/(i+1)
    return round(H,2)
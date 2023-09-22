def soma_h(num):
    '''
    	Função que calcula e retorna o valor de H com N termoss onde N é inteiro e dado como entrada.
        int -> float
    '''
    result=0
    for i in range(1,num+1):
        result+=1/i
    return round(result,2)
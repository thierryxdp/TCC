def soma_h(num):
    '''
    	Função que calcula e retorna o valor de H com N termoss onde N é inteiro e dado como entrada.
        int -> float
    '''
    result=0
    lista=[]
    for i in range(1,num):
        lista.append(1/i)
    return lista
def fatorial(num):
    '''
    	Função que, dado um número como
        parâmetro de entrada, retorna 
        o fatorial desse número
        : param num: int
        : return: int
    '''
    fatorial = num
    contador = 1
    
    while num-contador > 0:
        fatorial = fatorial*(num-contador)
        contador+=1
    
    return fatorial
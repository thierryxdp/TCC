def qtd_divisores (numero):
    '''
    	Função que conta quantos divisores tem um numero
        int -> int
    '''
    divisores = []
    i=0
    for i in numero:
        if numero%i==0:
            divisores = divisores + i
    return divisores
def repetidos(x):
    '''
    Função que dada uma lista de números, retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior
    list-> int
    '''
    x = []
    i = 0
    g = 1
    while i<len(x):      
    	if x[i] == x[g]:
        	repetido = 1
    	i=i+1 and g=g+1
        return repetido
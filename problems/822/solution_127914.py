def repetidos(x):
    '''
    Função que dada uma lista de números, retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior
    list-> int
    '''
    x = []
    i = 0
    a = 0
    while i<len(x):
        if x[i] == x[i+1]:
            a = 1
			return a
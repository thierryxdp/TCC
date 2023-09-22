def repetidos(x):
    '''
    Função que dada uma lista de números, retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior
    list-> int
    '''
    pares = 2
    i = 0
    while i<len(x):
        if x[i] == x[i+1]:
            i = i+1
        	pares = pares in (x[i]==x[i+1])
        return pares
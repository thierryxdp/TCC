def repetidos (lista):
    '''dada uma lista de numeros, retorna o numero de vezes que um elemento da lista é igual ao elemento anterior
       : list -> int
    '''
    qtd_repetidos = 0
    i = 1
    while i < len(lista):
        
        if lista[i] == lista[i-1]:
            qtd_repetidos = qtd_repetidos + 1
        i=i+1
    return qtd_repetidos
def repetidos(lista_num):
    '''
    	Funcao que recebe uma lista de numeros e retorna o 
        numero de vezes que um elemento da lista é igual
        ao elemento anterior
        list -> int
    '''
    i = 0
    qtd_vezes = 0
    while i < len(lista_num):
        if lista_num[i] == lista_num[i - 1]:
            qtd_vezes += 1
            i += 1
        else:
            i += 1
    return qtd_vezes
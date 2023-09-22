def repetidos(lista_num):
    '''
    	Função que recebe como entrada uma lista de números,
        e retorne o número de vezes que um elemento da lista 
        é igual ao elemento anterior.
    	i:int
        x:int
        contador:int
        lista_num:list
        return:int
    '''
    x = 1
    contador = 0
    i=0
    while i < len(lista_num)-1:
        if lista_num[i] == lista_num[i+x]:
            contador += 1
        i+=1
    return contador
def repetidos(lista_num):
    '''Recebe uma lista de numeros (lista_num),
    e retorna o numero de repetidos
    
    list -> int
    '''
    
    contador = 0 
    vezes = 0 
    
    while len(lista_num) > contador:
        if lista_num[contador] == lista_num[contador - 1]:
            vezes += 1
            contador += 1
        else: 
            contador += 1
    return vezes
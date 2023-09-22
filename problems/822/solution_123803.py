def repetidos(list):
    '''função que dada como parametro uma lista de numeros 
    inteiros,retorna o número de vezes que um elemento da lista é
    é igual ao elemento anterior
    list->int'''
    posicao=0
    repetido=0
    while posicao<len(list)-1:
        if list[posicao]==list[posicao]:
        posicao=posicao+1
    return repetido
def repetidos(lista):
    '''Calcula e retorna o numero de vezes em que um elemento é igual ao seu antecessor
       parameters:
       lista: lista original
    list->int'''
    posicao=0
    repeticao=0
    while posicao<len(lista):
        if lista[posicao]==lista[posicao-1]:
            repeticao=repeticao+1
        posicao=posicao+1
    return repeticao
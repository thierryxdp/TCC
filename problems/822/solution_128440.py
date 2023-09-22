def repetidos(lista):
    ''' Uma função que dado uma lista de números retorna 
    a quantidade de números repetidos da lista; list->int'''
    posicao=0
    repeticoes=0
    while posicao<len(lista):
        if lista[posicao]==lista[posicao+1]:
            repeticoes+=1
        posicao+=1
    return repeticoes
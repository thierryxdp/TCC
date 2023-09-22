def repetidos(lista):
    '''função que recebe uma lista de números e retornas quantas
    	repetições há nela.
        list -> int'''
    repeticao=0
    posicao=0
    while posicao<len(lista)-1:
        if lista[posicao]==lista[posicao+1]:
            repeticao=repeticao+1
        posicao+=1
    return repeticao
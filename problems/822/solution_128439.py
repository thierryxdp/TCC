def repetidos(lista):
    ''' Uma função que dado uma lista de números retorna 
    a quantidade de números repetidos da lista; list->int'''
    posiçao=0
    repetiçoes=0
    while posiçao<len(lista):
        if lista[posiçao]==lista[posiçao+1]:
            repetiçoes+=1
        posiçao+=1
    return repetiçoes
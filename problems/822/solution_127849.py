def repetidos(lista):
    '''Função que recebe uma lista e mostra quantas 
    vezes os números repetiram em sequência.
    list->int'''
    
    i=0
    x=0
    while i<len(lista):
        if lista [i]==lista[i-1]:
            x=x+1
    return x
def repetidos(lista):
    '''Função que recebe uma lista de números e 
    retorna o número de vezses que um elemento é igual ao anterior
    list->int
    '''
    i=1
    c=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            c+=1
        i+=1
    return c
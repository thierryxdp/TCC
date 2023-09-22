def repetidos(lista):
    '''Retorna o número de vezes que um elemento
    da lista é igual ao anterior
    list->int'''
    i=1
    ocorrencia=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            ocorrencia=ocorrencia+1
            
    return ocorrencia
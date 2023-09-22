def repetidos(lista):
    '''Função que recebe uma lista de numeros e retorna a quantidade de vezes
    que um elemento da lista é igual ao elemento anterior'''
    
    cont = 1
    ocorrencias = 0
    
    while(cont < len(lista)):
        if lista[cont] == lista[cont-1]:
            ocorrencias += 1
    
        cont += 1
    
    return ocorrencias
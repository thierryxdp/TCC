def repetidos(lista):
    '''função que recebe uma lista de numeros e retorna o numero de vezes 
    que um elemento da lusta é igual ao elemento anterior'''
    i=1
    result=0
    while i<len(lista):
        if lista[i]==lista[(i-1)]:
            result=result+1
        i=i+1
    return result
def repetidos(lista):
    '''Funcao que, dada uma lista de numeros, retorna o numero de vezes que um elemento é igual ao anterior; list[float,...] -> int'''  
    i=0
    contador=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            contador+=1
        i+=1
    return contador
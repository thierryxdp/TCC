def repetidos(lista):
    '''função que recebe como entrada uma lista de numeros e retorna 
    o valor inteiro indicando o numero de vezes em que um numero da lista
    é igual ao numero de indice anterior na lista; list->int'''
    
    i=1
    n=0
    
    while i<len(lista):
        if lista[i]==lista[i-1]:
            n=n+1
        i=i+1
    return n
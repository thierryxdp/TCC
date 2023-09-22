def repetidos(lista):
    '''Coloque uma lista de números e o resultado será o número de vezes que um número é igual ao seu antecessor
       list->int'''
    i=0
    l=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            l=l+1
        i=i+1
    return l
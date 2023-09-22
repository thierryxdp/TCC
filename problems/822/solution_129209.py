def repetidos(lista):
    '''Dado uma lista de números, retorna o número de vezes que
    um elemento da lista é igual seu antecessor. list-> int'''
    i=1
    c=0
    while i< len(lista)+1:
        if lista[i]==lista[i-1]:
            c+=1
        i+=1
    return c
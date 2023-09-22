def repetidos(lista):
    '''Recebe uma lista de números;
Retorna o número de vezes que um elemento da lista é igual ao anterior;
list => int'''
    x = 0
    i = 1
    while i<len(lista):
        if lista[i]==lista[i-1]:
            x = x+1
        i = i+1
    return x
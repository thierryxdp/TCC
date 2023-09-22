def repetidos(lista):
    ''' Essa função recebe uma lista de números, e retorna o número de vezes que um elemento é igual ao anterior;
    list -> int. '''
    x=0
    i=0
    while i <len(lista):
        if lista[i]== lista [i-1]:
            x=x+1
        i=i+1
    return x
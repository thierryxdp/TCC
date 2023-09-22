def repetidos(lista):
    '''Retorna o número de vezes que um elemento da lista é igual ao elemento anterior
list -> int'''
    i=0
    repeticoes=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repeticoes=repeticoes+1
        i=i+1
    return repeticoes
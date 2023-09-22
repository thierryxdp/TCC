def repetidos(lista):
    '''Recebe uma lista de números e retorna o numero de vezes que um elemento da lista é igua ao elemento
    anterior'''
    i=0
    repeticoes=0
    while len(lista)>i:
        if lista[i]==lista[i+1]:
            repeticoes=repeticoes+1
        i=i+1
    return repeticoes
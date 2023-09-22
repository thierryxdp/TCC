def repetidos(lista):
    '''dada uma lista de números, retorna o número de vezes que um elemento da lista é igual ao elemento anterior;
    list --> int'''
    prox=0
    num=0
    while prox<len(lista):
        if prox!=len(lista)-1:
            if lista[prox]==lista[prox+1]:
                num=num+1
        prox=prox+1
    return num
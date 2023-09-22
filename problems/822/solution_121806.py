# função repetidos

def repetidos(lista):
    '''Dada uma lista, retorna o número de vezes que um elemento da lista é igual ao elemento anterior.
    list -> int'''
    i=1
    q = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            q+=1
        i+=1
    return q
def repetidos(lista):
    '''Função que recebe uma lista de números(lista);
Retorna um int referindo-se ao número de vezes que um elemento da lista é igual ao elemento anterior.
list-> int'''
    i = 0
    r = []
    while i<len(lista):
        if lista[i]==lista[i-1]:
            r.append(lista[i])
            i = i+1
        else:
            i = i+1
    return len(r)
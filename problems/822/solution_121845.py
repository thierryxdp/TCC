def repetidos(l):
    '''Dada uma lista de numeros retorna o número de vezes que um elemento da lista é igual ao elemento anterior.
    list -> int'''
    i = 0
    cont = 0
    while i < (len(l)-1):
        if l[i] == l[i+1]:
            cont = cont + 1
        i = i + 1
    return cont
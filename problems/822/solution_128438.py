def repetidos(l):
    ''' retorna o número de vezes que um elemento da lista é igual ao elemento anterior, dada uma lista de números;
    list -> int '''
    i = 1
    x=0
    while i<len(l):
        if l[i]==l[i-1]:
            x= x+1
        i = i+1
    return x
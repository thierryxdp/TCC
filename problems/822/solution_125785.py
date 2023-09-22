def repetidos(lista):
    ''' funcao recebe uma lista e informa a quantidade  
   de vezes que um elemento da lista é igual ao elemento anterior
   lista-->int'''
    i=1
    s=0
    while i+1<len(lista):
        if lista[i]==lista[i+1]:
            s= s+1
        i=i+1
    return s
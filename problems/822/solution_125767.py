def repetidos(lista):
    ''' funcao recebe uma lista e informa a quantidade  
   de vezes que um elemento da lista é igual ao elemento anterior
   lista-->int'''
    i=1
    s=0
    while i<len(lista):
        if lista[s]==lista[s+1]:
            s= s+1
        s=s+1
        return i
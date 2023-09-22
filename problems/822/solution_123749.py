def repetidos(lista):
    ''' funcao que retorna o numero de vezes que um elemento é igual ao
        anterior list->int'''
    i=1
    a=0
    b=0
    while i+1<=len(lista):
        if lista[b]==lista[i]:
           a+=1
        i+=1
        b+=1
    return a
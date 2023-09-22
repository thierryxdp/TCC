def repetidos(lista):
    '''...'''
    r=()
    i=0
    
    while i<len(lista):
        if lista[i]==lista[i]-1:
            list.pop(lista, [i])
           
        i+=1
    return r
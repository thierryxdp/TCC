def repetidos(lista):
    '''...'''
    r=''
    i=0
    
    while i<len(lista):
        if lista[i]==lista[i]-1:
            list.pop(lista, [i])
            list.append(r, list.pop())
        i+=1
    return r
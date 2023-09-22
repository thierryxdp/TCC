def repetidos(lista):
    ''' list -> int'''
    i=0
    x=0
    while i < len (lista)-1:
        if lista[i]==lista[i+1]:
            x+=1
        i+=1
    return x
def repetidos(lista):
    '''list-->str'''
    a=1
    b=0
    while a<len(lista):
        if lista[a]==lista[a-1]:
            b+=1
        a+=1
    return b
def repetidos(lista):
    '''conta quantas vezes o numero anterior é igual o numero da frente. list->int'''
    i=0
    a=0
    b=[]
    while i<len(lista):
        if lista[i] == lista[i-1]:
            a=a+1
            b.append(a)
        i=i+1
    return b[-1}
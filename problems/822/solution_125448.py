def repetidos(lista):
    '''retorna quantas vezes um numero da lista e igual ao anterior
       list -> int'''
    a=1
    b=0
    while a<len(lista):
        if lista[a]==lista[a-1]:
            b=b+1
        a=a+1
    return b
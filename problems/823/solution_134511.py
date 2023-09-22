def faltante(lista):
    '''Dado uma lista contendo numeros sequenciais, retorna qual numero falta para completar a sequencia da lista.list->int'''
    a=1
    b=0
    while a<len(lista):
        if lista[a]-lista[a-1]!=1:
            b=lista[a-1]+1
        a=a+1
    if len(lista)==1:
        if lista[0]>1:
            b=lista[0]-1
        else:
            b=lista[0]+1
    if b==0:
        if 1 in lista:
            b=a+1
        else:
            b=1
    return b
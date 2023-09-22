def repetidos(lista):
    '''Dado uma lista de números. Retorna o número de vezes que um
elemento da lista é igual ao elemento anterior. list-->int'''
    i=0
    num=1
    while num<len(lista):
        if lista[num]==lista[num-1]:
            i=i+1
            num=num+1
    return i
def repetidos(lista_num):
    '''Função que retorna o número de vezes que um elemento da 
    lista é igual ao elemento anterior.
    lista_num=list->list'''
    y=0
    z=0
    while y<len(lista_num):
        if lista_num[y]==lista_num[y-1]:
            z=z+1
        y=y+1
    return z
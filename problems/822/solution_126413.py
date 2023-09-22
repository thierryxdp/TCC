def repetidos(lista_num):
    '''Retorna o número de vezes que um elemento da lista é igual ao elemento anterior, list -> int'''
    vezes=0
    i=1
    while i<len(lista_num):
        if lista_num[i]==lista_num[i-1]:
            vezes+=1
            i+=1
        else:
            i+=1
    return vezes
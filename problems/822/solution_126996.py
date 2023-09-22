def repetidos(lista):
    '''função que recebe como entrada uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior; list -> int'''
    i=1
    z=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            z+=1
        i=i+1
    return z
def repetidos(lista):
    '''funcao que recebe uma lista de numeros como entrada e retorna o numero de vezes que um elemento da lista e igual ao elemento anterior
    list -> int'''
    i=1
    indice=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            indice=indice+1
        i=i+1
    return indice
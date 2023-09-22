def repetidos(lista):
    '''Funcao que recebe uma lista de numeros e retorna o numero de vezes que 
    um elemento da lista é igual ao elemento anterior
    list->int'''
    a=0
    b=0
    while a<len(lista):
        if lista[a]==lista[a-1]:
            b=b+1
        a=a+1
    return b
def repetidos(lista):
    '''
Função que recebe uma lista de números e retorna o número
de vezes que um elemento da lista  é igual ao elemento anterior.

list-->int
    '''
    i=0
    while i<len(lista):
        a=lista[i:]==lista[i+1:]
        list.count(a)
    return a
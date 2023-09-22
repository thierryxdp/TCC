def repetidos(lista):
    '''Função que recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior;
    list->int'''
    contador = 0
    vezes = 0
    while contador<len(lista):
        if lista[i] == lista[i-1]:
            vezes=vezes+1
        else:
            vezes=vezes
            i=i+1
    return vezes
def repetidos(lista=[]):
    '''função que recebe uma lista de números e retorna o número
    de vezes que um elemento da lista é igual ao seu anterior'''
    valor = 0
    for i in range(len(lista)):
        if i > 0 and lista[i]==lista[i-1]:
            valor+=1
    return valor
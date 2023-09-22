def repetidos(lista):
    '''dado uma lista, retorna o números de vezes que um elemento é igual ao seu antecessor
    lista->int'''
    i=1
    soma=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            soma+=1
    return soma
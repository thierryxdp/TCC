def repetidos(lista):
    '''Função que recebe como entrada uma lista de números e
retorna o número de vezes que um elemento da lista é igual ao anterior.
    list-->int'''
    i = 0
    contador = 0
    while i <len(lista):
        if lista[i-1]==lista[i]:
            contador = contador +1
        i =i+1
    return contador
def repetidos(lista):
    '''recebe uma lista de numeros e retorna a quantidade de vezes
    em que um numero da lista é igual ao anterior
    list->int'''
    
    contador = 1
    teste = 0
    while contador<len(lista):
        if lista[contador]==lista[contador-1]:
            teste = teste+1
        contador = contador +1
    return teste
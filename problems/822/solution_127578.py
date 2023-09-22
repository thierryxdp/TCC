def repetidos(lista):
    '''funcao que recebe uma lista de numeros e retorna o numero de vezes que teve teve o maior numero repetido dentro da lista
    list>list'''
    i=0
    while i<len(lista):
        if lista[i] in lista:
            lista=list.count(i)
        i=i+1
    return i